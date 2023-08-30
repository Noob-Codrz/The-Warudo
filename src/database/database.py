# import dependencies
import os
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
import databases

# load environment variables from .env file
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
database = databases.Database(DATABASE_URL)
engne = sqlalchemy.create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engne)
Base = declarative_base()

def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()
