from sqlalchemy import Column, Integer, String, DECIMAL, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from .db import Base

class UserType(enum.Enum):
    CUSTOMER = "CUSTOMER"
    MERCHANT = "MERCHANT"

class TransactionStatus(enum.Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    balance = Column(DECIMAL(15, 2), default=0.00)
    user_type = Column(Enum(UserType), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    customer_transactions = relationship("Transaction", foreign_keys="[Transaction.customer_id]")
    merchant_transactions = relationship("Transaction", foreign_keys="[Transaction.merchant_id]")

class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    merchant_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    amount = Column(DECIMAL(15, 2), nullable=False)
    status = Column(Enum(TransactionStatus), default=TransactionStatus.PENDING)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

class BalanceHistory(Base):
    __tablename__ = "balance_history"
    history_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    change_amount = Column(DECIMAL(15, 2), nullable=False)
    new_balance = Column(DECIMAL(15, 2), nullable=False)
    reason = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
