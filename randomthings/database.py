from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base

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


class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "name='%s', fullname='%s', nickname='%s'" % (
            self.name, self.fullname, self.nickname)




Base.metadata.create_all(engine)
