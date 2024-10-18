from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql+mysqlconnector://user:@localhost/my_library")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

def get_db():

    db = SessionLocal()
    return db  