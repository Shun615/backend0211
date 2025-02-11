from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


# ## SQLite用のコード ###

# class Base(DeclarativeBase):
#     pass


# class Customers(Base):
#     __tablename__ = 'customers'
#     customer_id: Mapped[str] = mapped_column(primary_key=True)
#     customer_name: Mapped[str] = mapped_column()
#     age: Mapped[int] = mapped_column()
#     gender: Mapped[str] = mapped_column()


# class Items(Base):
#     __tablename__ = 'items'
#     item_id: Mapped[str] = mapped_column(primary_key=True)
#     item_name: Mapped[str] = mapped_column()
#     price: Mapped[int] = mapped_column()


# class Purchases(Base):
#     __tablename__ = 'purchases'
#     purchase_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     purchase_name: Mapped[str] = mapped_column(ForeignKey("customers.customer_id"))
#     date: Mapped[datetime] = mapped_column()


# class PurchaseDetails(Base):
#     __tablename__ = 'purchase_details'
#     purchase_id: Mapped[int] = mapped_column(ForeignKey("purchases.purchase_id"), primary_key=True)
#     item_name: Mapped[str] = mapped_column(ForeignKey("items.item_id"), primary_key=True)
#     quantity: Mapped[int] = mapped_column()



### MySQL用のコード ###

class Base(DeclarativeBase):
    pass


class Customers(Base):
    __tablename__ = 'customers'
    customer_id: Mapped[str] = mapped_column(String(100), primary_key=True)
    customer_name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(10))


class Items(Base):
    __tablename__ = 'items'
    item_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    item_name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)


class Purchases(Base):
    __tablename__ = 'purchases'
    purchase_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    purchase_name: Mapped[str] = mapped_column(String(10), ForeignKey("customers.customer_id"))
    date: Mapped[datetime] = mapped_column(DateTime)


class PurchaseDetails(Base):
    __tablename__ = 'purchase_details'
    # ForeignKeyの使用が抜けておりました、申し訳ございません。
    purchase_id: Mapped[int] = mapped_column(Integer, ForeignKey("purchases.purchase_id"), primary_key=True)
    item_name: Mapped[str] = mapped_column(String(10), ForeignKey("items.item_id"), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer)
