from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import CheckConstraint
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
    book_author: Mapped[int] = mapped_column()
    release_year: Mapped[datetime] = mapped_column(DateTime)
    price: Mapped[int] = mapped_column()
    sold_amount: Mapped[int] = mapped_column()
    
    
    __table_args__ = (
        CheckConstraint(price >= 0, name='check_price_positive'),
        CheckConstraint(sold_amount >= 0, name='check_sold_amount_positive')
    )