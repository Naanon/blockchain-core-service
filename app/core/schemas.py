from pydantic import BaseModel, Field
from typing import List
from typing import Optional

class WalletCreate(BaseModel):
    quantity: int

class WalletResponse(BaseModel):
    address: str

class TxValidationRequest(BaseModel):
    tx_hash: str

class TransferInfo(BaseModel):
    asset: str
    to_address: str
    value: float

class TxValidationResponse(BaseModel):
    is_valid: bool
    transfers: List[TransferInfo]

class HistoryResponse(BaseModel):
    tx_hash: str
    from_address: str
    to_address: str
    value: float
    asset: str

class CreateTransactionRequest(BaseModel):
    from_address: str
    to_address: str
    asset: str = Field(..., description="Ex: 'ETH', 'USDC'")
    value: float = Field(..., gt=0, description="Valor em formato decimal, ex: 0.005")

class CreateTransactionResponse(BaseModel):
    status: str
    tx_hash: Optional[str] = None
    message: str

class OutgoingHistoryResponse(BaseModel):
    tx_hash: Optional[str]
    from_address: str
    to_address: str
    asset: str
    value: float
    status: str

class Config:
    orm_mode = True

        