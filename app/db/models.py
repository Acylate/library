from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Library(Base):
    __tablename__ = "library"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    book_name: Mapped[str] = mapped_column(String(100))
    book_author: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    release_year: Mapped[int] = mapped_column()
    price: Mapped[float] = mapped_column()
    sold_amount: Mapped[int] = mapped_column()
    
    __table_args__ = (
        CheckConstraint(price >= 0, name='check_price_positive'),
        CheckConstraint(sold_amount >= 0, name='check_sold_amount_positive')
    )

  
class Authors(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(60))
    birth_year: Mapped[int] = mapped_column()
    birth_city: Mapped[str] = mapped_column(String(30))


class Transaction(Base):
    __tablename__ = "transaction"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(30))
    book_id: Mapped[int] = mapped_column(ForeignKey("library.id"))
    buy_price: Mapped[float] = mapped_column(nullable=True)
    sell_price: Mapped[float] = mapped_column(nullable=True)
    book_amount: Mapped[int] = mapped_column()
    
    __table_args__ = (
        CheckConstraint(buy_price >= 0, name='check_buy_price_positive'),
        CheckConstraint(book_amount >= 0, name='check_book_amount_positive'),
        CheckConstraint(sell_price >= 0, name='check_sell_price_positive')
    )


class Bank(Base):
    __tablename__ = "bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    transaction: Mapped[int] = mapped_column(ForeignKey("transaction.id"))
    balance: Mapped[float] = mapped_column()
    balance_change: Mapped[float] = mapped_column()
    current_balance: Mapped[float] = mapped_column()
