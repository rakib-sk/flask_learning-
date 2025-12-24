from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Table, Column
from typing import Optional, List
from datetime import datetime,timezone

app = Flask(__name__)

app.config["SECRET_KEY"] = "my-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy()
db.init_app(app)

class Base(DeclarativeBase):
    pass
    
class Customer(Base):
    __tablename__="customer"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] =  mapped_column(String(50))
    address: Mapped[str] = mapped_column(String(500))
    city: Mapped[str] = mapped_column(String(50))
    postcode: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50),unique=True)
        
    customer_orders: Mapped[List["CustomerOrder"]] = relationship(back_populates="customer")
        
        
customer_order_product = Table(
    "customer_order_product",
    Base.metadata,
    Column("customer_order_id",ForeignKey("customer_order.id"),primary_key=True),
    Column("product_id",ForeignKey("product.id"),primary_key=True)
)        
        
    
class CustomerOrder(Base):
    __tablename__="customer_order"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))        
    order_date: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    shipped_date: Mapped[Optional[datetime]]
    deriverd_date: Mapped[Optional[datetime]]
    coupon_code: Mapped[Optional] = mapped_column(String(50))
    customer: Mapped["Customer"] = relationship(back_populates="customer_orders")    
    product: Mapped[List["Product"]] = relationship(secondary="customer_order_product",back_populates="customer_orders")        
        


class Product(Base):
    __tablename__="product"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),unique=True)
    price: Mapped[int]  
    customer_orders: Mapped[List["CustomerOrder"]] = relationship(secondary="customer_order_product",back_populates="product")
        
        
        
        
with app.app_context():
    Base.metadata.create_all(db.engine)
    db.create_all()
    print("Tables created!")
    
    customers = [
        Customer(first_name="Sanjida", last_name="Aktar", address="Chapai", city="Chapai", postcode="123", email="sanjidaakter@gmail.com"),
        Customer(first_name="Alfi", last_name="Tabassum", address="Jashore", city="Jahore", postcode="567", email="alfitabssum@gmail.com"),
        Customer(first_name="Hanjala", last_name="Trader", address="Jhinidha", city="Jhi", postcode="123", email="hanjalatrader@gmail.com"),
        Customer(first_name="Rahim", last_name="Uddin", address="Dhaka", city="Dhaka", postcode="1000", email="rahimuddin@gmail.com"),
        Customer(first_name="Karim", last_name="Ali", address="Chittagong", city="Chittagong", postcode="4000", email="karimali@gmail.com"),
        Customer(first_name="Sakib", last_name="Hasan", address="Sylhet", city="Sylhet", postcode="3100", email="sakibhasan@gmail.com"),
        Customer(first_name="Tamim", last_name="Iqbal", address="Rajshahi", city="Rajshahi", postcode="6000", email="tamimiqbal@gmail.com"),
        Customer(first_name="Mushfiq", last_name="Urichpur", address="Barisal", city="Barisal", postcode="8200", email="mushfiqurich@gmail.com"),
        Customer(first_name="Liam", last_name="Noah", address="Khulna", city="Khulna", postcode="9000", email="liamnoah@gmail.com"),
        Customer(first_name="Olivia", last_name="Ava", address="Mymensingh", city="Mymensingh", postcode="2200", email="oliviaava@gmail.com"),
    ]
    
    db.session.add_all(customers)
    db.session.commit()
    print("10 customers added!")


  