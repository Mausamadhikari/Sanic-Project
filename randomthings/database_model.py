from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import ForeignKey

DATABASE = {
    'type': 'postgresql',
    'host': 'localhost',
    'user': 'postgres',
    'port': '5432',
    'password': 'myPassword',
    'database': 'postgres'
}

conn_uri = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
    'postgresql',
    DATABASE['user'], DATABASE['password'], DATABASE['host'],
    DATABASE['port'], DATABASE['database'])


engine = create_engine(conn_uri)
connection = engine.connect()

Base = declarative_base()


class Brand(Base):
    name = Column(String)
    image = Column(String)
    

class Unit(Base):
    pass


class Category(Base):
    pass


class Product(Base):
    pass


class SKU(Base):
    pass


class Batch(Base):
    id = Column(String, autoincrement=True, unique=True, primary_key=True)
    sku_id = Column(Integer, ForeignKey(SKU.id))
