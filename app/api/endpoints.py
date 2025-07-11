from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core import schemas
from app.services import wallet as wallet_service
from app.database.database import SessionLocal, engine
from app.services import transaction as tx_service
from app.database import models
from app.services import sender as sender_service

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/wallets", tags=["Wallets"])
def create_wallets(request: schemas.WalletCreate, db: Session = Depends(get_db)):
    result = wallet_service.generate_wallets(db=db, quantity=request.quantity)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@router.get("/wallets", response_model=List[schemas.WalletResponse], tags=["Wallets"])
def list_wallets(db: Session = Depends(get_db)):
    wallets = wallet_service.get_all_wallets(db=db)
    return wallets

@router.post("/transactions/validate", response_model=schemas.TxValidationResponse, tags=["Transactions"])
def validate_transaction(request: schemas.TxValidationRequest, db: Session = Depends(get_db)):
    models.Base.metadata.create_all(bind=engine)
    
    result = tx_service.validate_and_store_transaction(db, request.tx_hash)
    return result

@router.get("/transactions/history", response_model=List[schemas.HistoryResponse], tags=["Transactions"])
def get_transaction_history(db: Session = Depends(get_db)):
    history = tx_service.get_history(db)
    return history

@router.post("/transactions/send", response_model=schemas.CreateTransactionResponse, tags=["Transactions"])
def send_new_transaction(request: schemas.CreateTransactionRequest, db: Session = Depends(get_db)):
    models.Base.metadata.create_all(bind=engine)
    
    result = sender_service.send_transaction(db=db, request=request)
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.get("/transactions/outgoing", response_model=List[schemas.OutgoingHistoryResponse], tags=["Transactions"])
def list_outgoing_transactions(db: Session = Depends(get_db)):
    return sender_service.get_outgoing_history(db)