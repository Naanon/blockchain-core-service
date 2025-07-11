import traceback
from web3 import Web3
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database import models
from app.services import wallet as wallet_service

w3 = Web3(Web3.HTTPProvider(settings.NODE_PROVIDER_URL))

# ABI Mínimo para funções de nome, símbolo e decimais de um token ERC20
MINIMAL_ERC20_ABI = [
    {"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},
    {"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},
    {"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},
]

def validate_and_store_transaction(db: Session, tx_hash: str):
    try:
        existing_tx = db.query(models.ValidatedTransaction).filter(models.ValidatedTransaction.tx_hash == tx_hash).first()
        if existing_tx:
            return {"is_valid": True, "transfers": [], "message": "Transaction already validated."}

        tx = w3.eth.get_transaction(tx_hash)
        receipt = w3.eth.get_transaction_receipt(tx_hash)

        if not receipt or receipt['status'] != 1:
            return {"is_valid": False, "transfers": []}
        
        our_wallets_db = wallet_service.get_all_wallets(db)
        our_addresses = {w.address for w in our_wallets_db}

        transfers = []
        is_for_us = False
        
        tx_input_hex = tx['input'].hex()
        tx_to_address = tx['to']

        if (tx_input_hex == '0x' or tx_input_hex == '') and tx_to_address in our_addresses:
            is_for_us = True
            value = w3.from_wei(tx['value'], 'ether')
            transfers.append({"asset": "ETH", "to_address": tx_to_address, "value": float(value)})
            
            new_tx = models.ValidatedTransaction(
                tx_hash=tx_hash, from_address=tx['from'], to_address=tx_to_address,
                value=float(value), asset="ETH"
            )
            db.add(new_tx)

        elif tx_input_hex.startswith('0xa9059cbb'):
            recipient_hex = '0x' + tx_input_hex[34:74]
            checksum_recipient = Web3.to_checksum_address(recipient_hex)
            
            if checksum_recipient in our_addresses:
                is_for_us = True
                token_contract = w3.eth.contract(address=tx_to_address, abi=MINIMAL_ERC20_ABI)
                decimals = token_contract.functions.decimals().call()
                symbol = token_contract.functions.symbol().call()
                amount_wei = int(tx_input_hex[74:], 16)
                value = amount_wei / (10 ** decimals)

                transfers.append({"asset": symbol, "to_address": checksum_recipient, "value": value})
                
                new_tx = models.ValidatedTransaction(
                    tx_hash=tx_hash, from_address=tx['from'], to_address=checksum_recipient,
                    value=value, asset=symbol
                )
                db.add(new_tx)

        if is_for_us:
            db.commit()
            return {"is_valid": True, "transfers": transfers}
        else:
            return {"is_valid": False, "transfers": []}

    except Exception as e:
        import traceback
        print(f"Erro inesperado durante a validação: {e}")
        traceback.print_exc()
        return {"is_valid": False, "transfers": []}


def get_history(db: Session):
    return db.query(models.ValidatedTransaction).all()