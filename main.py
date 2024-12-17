from fastapi import FastAPI 
from src import data_base
from src.domain import model


app = FastAPI()


@app.get('/categories', tags=['categories'])
def get_categories():
    with data_base.Session(bind = data_base.engine) as session:
        categ = session.query(data_base.Categories).all()
        return categ


@app.get('/categories/{id}', tags=['categories'])
def serch_categories(id: int):
    with data_base.Session(bind= data_base.engine) as session:
        categ = session.get(data_base.Categories, id)
        if categ:
            return categ
        else:
            return {'Category': 'not found'}


@app.post('/categoires', tags=['categories'])
def add_categories(category: model.Category):
    categ = data_base.Categories(name = category.category_name)
    with data_base.Session(bind=data_base.engine) as session:
        session.add(categ)
        session.commit()
        session.refresh(categ)
        return {'Category': 'has beeen added'}
   

@app.put('/categories/', tags=['categories'])
def update_categories(id: int, category: model.Category):
    new_data = data_base.Categories(name = category.category_name)
    with data_base.Session(bind=data_base.engine) as session:
        categ = session.query(data_base.Categories).get(id)
        if categ:
            categ.name = new_data.name
            session.add(categ)
            session.commit()
            session.refresh(categ)
            return {'Category': 'has been updated'}
        else:
            return {'Category': 'not found'}
    

@app.delete('/categories/{id}', tags=['categories'])
def delete_categories(id: int):
    with data_base.Session(bind= data_base.engine) as session:
        categ = session.get(data_base.Categories, id)
        if categ:
            session.delete(categ)
            session.commit()
            return {'Category': 'has been deleted'}
        else:
            return {'Category': 'not found'}
        



@app.get('/products', tags=['products'])
def get_products():
    with data_base.Session(bind = data_base.engine) as session:
        prod = session.query(data_base.Products).all()
        return prod


@app.get('/products/{id}', tags=['products'])
def serch_product(id: int):
    with data_base.Session(bind=data_base.engine) as session:
        prod = session.get(data_base.Products, id)
        if prod:
            return prod
        else:
            return{'Product':'not found'}


@app.post('/products', tags=['products'])
def add_products(product: model.Product):
    prod = data_base.Products(name= product.product_name,
                              category_id = product.category_id,
                              availability = product.availability, 
                              price = product.price, 
                              description = product.description
                              )
    with data_base.Session(bind=data_base.engine) as session:
        session.add(prod)
        session.commit()
        session.refresh(prod)
        return {'Product': 'has been added'}


@app.put('/products/{id}', tags=['products'])
def update_products(id: int, product: model.Product):
    new_prod= data_base.Products(name= product.product_name,
                              category_id = product.category_id,
                              availability = product.availability, 
                              price = product.price, 
                              description = product.description
                              )
    with data_base.Session(bind=data_base.engine) as session:
        prod= session.query(data_base.Products).get(id)
        if prod:
            prod.name = new_prod.name
            prod.category_id = new_prod.category_id
            prod.availability = new_prod.availability
            prod.price = new_prod.price
            prod.description = new_prod.description
            session.add(prod)
            session.commit()
            session.refresh(prod)
            return {'Product': 'has beem updated'}
        else:
            return {'Product':'not found'}
        

@app.delete('/products/{id}', tags=['products'])
def delete_products(id: int):
    with data_base.Session(bind=data_base.engine) as session:
        prod = session.get(data_base.Products, id)
        if prod:
            session.delete(prod)
            session.commit()
            return {'Product':'has been deleted'}
        else:
            return {'Product':'not found'}