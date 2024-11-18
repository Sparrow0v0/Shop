from pydantic import BaseModel, EmailStr
from datetime import date



class Product(BaseModel):
    product_id: str = None 
    product_name: str 
    category_id: int 
    availability: int 
    price: float 
    description:str 
    reviews: list[str] = None
 

class Basket(BaseModel):   
        basket_id:int = None
        quantity:int 
        buyer_id:str
        products: list[Product] = None
        

class Order(BaseModel):
        order_id:int = None
        product_id:int  
        basket_id:int  
        date_order: date


class Buyer(BaseModel):
        buyer_id: int = None
        login:str 
        password:str
        buyer_name:str
        address:str 
        e_mail: EmailStr 
        basket_id: int
        order_history: list[Order] = None


class Category(BaseModel):
        category_id:int = None
        category_name:str
        
    
class Storage(BaseModel):
        storage_id:int = None
        storage_address:str 
        product_id:int 
        quantity:int