import enum
from sqlalchemy import Column, Integer, String, Float, Enum, UniqueConstraint
from .database import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True, nullable=False)
    private_key = Column(String, unique=True, nullable=False)

class ValidatedTransaction(Base):
    __tablename__ = "validated_transactions"

    id = Column(Integer, primary_key=True, index=True)
    tx_hash = Column(String, unique=True, index=True, nullable=False)
    from_address = Column(String, nullable=False)
    to_address = Column(String, nullable=False, index=True)
    value = Column(Float, nullable=False)
    asset = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint('tx_hash'),)

class TransactionStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    FAILED = "failed"

class OutgoingTransaction(Base):
    __tablename__ = "outgoing_transactions"

    id = Column(Integer, primary_key=True, index=True)
    tx_hash = Column(String, unique=True, index=True, nullable=True)
    from_address = Column(String, index=True, nullable=False)
    to_address = Column(String, index=True, nullable=False)
    asset = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    status = Column(Enum(TransactionStatus), nullable=False, default=TransactionStatus.PENDING)
    gas_price_wei = Column(String, nullable=True)
    gas_used = Column(String, nullable=True)