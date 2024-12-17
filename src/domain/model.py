from pydantic import BaseModel, EmailStr
from datetime import date



class Product(BaseModel):
     
    product_name: str 
    category_id: int 
    availability: int 
    price: float 
    description:str 

 

class Basket(BaseModel):   

        quantity:int 
        buyer_id:str
        products: list[Product] = None
        

class Order(BaseModel):

        product_id:int  
        basket_id:int  
        date_order: date


class Buyer(BaseModel):

        login:str 
        password:str
        buyer_name:str
        address:str 
        e_mail: EmailStr 
        basket_id: int
        order_history: list[Order] = None


class Category(BaseModel):

        category_name:str
        
    
class Storage(BaseModel):

        storage_address:str 
        product_id:int 
        quantity:int