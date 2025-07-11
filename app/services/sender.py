# Em app/services/sender.py
from web3 import Web3
from sqlalchemy.orm import Session
from decimal import Decimal, getcontext

from app.core.config import settings
from app.database import models
from app.core import schemas

getcontext().prec = 50

w3 = Web3(Web3.HTTPProvider(settings.NODE_PROVIDER_URL))

def send_transaction(db: Session, request: schemas.CreateTransactionRequest):
    from_wallet = db.query(models.Wallet).filter(models.Wallet.address == request.from_address).first()
    if not from_wallet:
        return {"status": "error", "message": "Source address not found in our wallet."}

    try:
        nonce = w3.eth.get_transaction_count(from_wallet.address)
    except Exception as e:
        return {"status": "error", "message": f"Failed to get nonce: {e}"}

    value_in_wei = int(Decimal(request.value) * Decimal(10**18))
    
    tx_data = {
        'from': from_wallet.address,
        'to': request.to_address,
        'value': value_in_wei,
        'nonce': nonce,
        'chainId': w3.eth.chain_id
    }
    
    if request.asset.upper() != 'ETH':
        return {"status": "error", "message": "Only ETH transfers are currently supported."}

    try:
        gas_estimate = w3.eth.estimate_gas(tx_data)
        tx_data['gas'] = int(gas_estimate * 1.2) # Margem de 20%
        tx_data['gasPrice'] = w3.eth.gas_price
    except Exception as e:
        return {"status": "error", "message": f"Gas estimation failed: {e}"}

    db_tx = models.OutgoingTransaction(
        from_address=request.from_address,
        to_address=request.to_address,
        asset=request.asset.upper(),
        value=request.value,
        status=models.TransactionStatus.PENDING,
        gas_price_wei=str(tx_data['gasPrice'])
    )
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    
    private_key = from_wallet.private_key
    try:
        signed_tx = w3.eth.account.sign_transaction(tx_data, private_key)
    except Exception as e:
        db_tx.status = models.TransactionStatus.FAILED
        db.commit()
        return {"status": "error", "message": f"Failed to sign transaction: {e}"}

    try:
        tx_hash = w3.eth.send_raw_transaction(signed_tx[0])
        db_tx.tx_hash = tx_hash.hex()
        db.commit()
    except Exception as e:
        db_tx.status = models.TransactionStatus.FAILED
        db.commit()
        return {"status": "error", "message": f"Transaction broadcast failed: {e}"}

    try:
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
        if receipt['status'] == 1:
            db_tx.status = models.TransactionStatus.CONFIRMED
            db_tx.gas_used = str(receipt['gasUsed'])
        else:
            db_tx.status = models.TransactionStatus.FAILED
        
        db.commit()
        return {"status": db_tx.status.value, "tx_hash": db_tx.tx_hash, "message": "Transaction processed."}

    except Exception as e:
        return {"status": "pending", "tx_hash": db_tx.tx_hash, "message": f"Transaction sent but confirmation timed out: {e}"}

def get_outgoing_history(db: Session):
    return db.query(models.OutgoingTransaction).all()