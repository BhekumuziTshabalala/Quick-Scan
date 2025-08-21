from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
import enum

# ---------- ENUMS ----------
class UserType(enum.Enum):
    CUSTOMER = "CUSTOMER"
    MERCHANT = "MERCHANT"

class TransactionStatus(enum.Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

# ---------- BASE ----------
Base = declarative_base()

# ---------- USERS TABLE ----------
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    balance = Column(DECIMAL(15, 2), default=0.00)
    user_type = Column(Enum(UserType), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime)

    # relationships
    customer_transactions = relationship("Transaction", foreign_keys="[Transaction.customer_id]")
    merchant_transactions = relationship("Transaction", foreign_keys="[Transaction.merchant_id]")

# ---------- TRANSACTIONS TABLE ----------
class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    merchant_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    amount = Column(DECIMAL(15, 2), nullable=False)
    status = Column(Enum(TransactionStatus), default=TransactionStatus.PENDING)
    created_at = Column(TIMESTAMP, default=datetime)

# ---------- BALANCE HISTORY TABLE ----------
class BalanceHistory(Base):
    __tablename__ = "balance_history"

    history_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    change_amount = Column(DECIMAL(15, 2), nullable=False)
    new_balance = Column(DECIMAL(15, 2), nullable=False)
    reason = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime)


# ---------- DATABASE CONNECTION ----------
engine = create_engine("sqlite:///../resources/payment_platform.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
