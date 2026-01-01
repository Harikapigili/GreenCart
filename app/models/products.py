from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime 
from sqlalchemy.sql import func
from app.database import Base
class Product(Base):
    __tablename__="products"
    id=Column(Integer, primary_key=True, index=True)
    product_name=Column(String(50),unique=True,index=True,nullable=False)
    description=Column(String(255),unique=True,nullable=False)
    price=Column(Float,nullable=False)
    quantity=Column(Integer,index=True,nullable=False)
    is_available=Column(Boolean,default=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),onupdate=func.now())