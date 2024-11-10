class Product:
   
    def __init__ (self, 
        name:str, 
        category:str,
        availability:int, 
        price:int, 
        description:str, 
        reviews:str
        ):
        self.product_id: int
        self.name = name
        self.category = category
        self.availbility = availability
        self.price = price
        self.description = description
        self.reviews = reviews
        


class Buyer:

    def __init__(self, 
        buyer_id:int,
        login:str, 
        password:str,
        name:str, 
        address:str, 
        e_mail:str, 
        basket_id, 
        order_history:str
        ):
        self.id = buyer_id
        self.login = login
        self.password = password
        self.name = name
        self.address = address
        self.e_mail = e_mail
        self.basket_id = basket_id
        self.order_history = order_history


class Basket:

    def __init__(self, 
        basket_id:int, 
        product_id:int, 
        product_name:str, 
        price:int, 
        availability:int, 
        quantity:int, 
        buyer_id:str, 
        buyer_name:str, 
        address:str
        ):
         self.id = basket_id
         self.product_id = product_id
         self.name = product_name
         self.price = price
         self.availbility = availability
         self.quantity = quantity
         self.buyer_id = buyer_id
         self.buyer_name = buyer_name
         self.address = address


class Order:

    def __init__(self, 
        order_id:int,
        product_id:int, 
        name_product:str, 
        price:int, 
        quantity:int, 
        address:str, 
        date_order:str
        ):
        self.id = order_id
        self.product_id = product_id
        self.name_product = name_product
        self.price = price
        self.quantity = quantity
        self.address = address
        self.date_order = date_order

class Category:

    def __init__(self, 
        category_id:int, 
        name:str
        ):
        self.id = category_id
        self.name = name


class Storage:

    def __init__(self, 
        storage_id:int, 
        storage_address:str, 
        product_id:int, 
        quantity:int, 
        supplier_id:int
        ):
        self.id = storage_id
        self.address = storage_address
        self.product_id = product_id
        self.quantity = quantity
        self.supplier_id = supplier_id


class Supplier:

    def __init__(self, 
        supplier_id:int, 
        supplier_name:str, 
        supply_history:str
        ):
        self.id = supplier_id
        self.name = supplier_name
        self.history = supply_history
