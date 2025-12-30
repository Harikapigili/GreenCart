from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional
class ProductBase(BaseModel):
    product_name:str=Field(...,min_length=3,max_length=50)
    description:str=Field(...,min_length=3,max_length=255)
    price:float
    quantity:int
    is_available:bool=True
class CreateProduct(ProductBase):
    pass 
class ProductResponse(ProductBase):
    id: int 
    class Config:
        from_attributes=True