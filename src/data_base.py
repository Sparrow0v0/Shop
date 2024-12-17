from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker



   
sqlite_database = "sqlite:///storebd.db"
   
engine = create_engine(sqlite_database)

Session = sessionmaker(autoflush=False, bind=engine)

class Base(DeclarativeBase): pass

with Session(autoflush=False, bind=engine):
    pass

class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key= True) 
    name = Column(String) 
    category_id = Column(Integer, ForeignKey(Categories.id)) 
    availability = Column(Integer) 
    price = Column(Integer) 
    description = Column(String) 

Base.metadata.create_all(engine)