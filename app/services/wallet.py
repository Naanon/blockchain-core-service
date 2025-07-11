from sqlalchemy.orm import Session
from web3 import Account
import os

from app.database import models

def generate_wallets(db: Session, quantity: int):
    if quantity <= 0:
        return {"error": "Quantity must be positive"}

    new_wallets = []
    for _ in range(quantity):
        account = Account.create(os.urandom(32))
        private_key = account.key.hex()
        address = account.address
        
        db_wallet = models.Wallet(address=address, private_key=private_key)
        db.add(db_wallet)
        new_wallets.append(db_wallet)

    db.commit()
    for wallet in new_wallets:
        db.refresh(wallet)
        
    return {"message": f"{quantity} new wallets created successfully."}


def get_all_wallets(db: Session):
    return db.query(models.Wallet).all()