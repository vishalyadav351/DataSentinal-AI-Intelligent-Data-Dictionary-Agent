from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse


my_password = urllib.parse.quote_plus("this area my password") 


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:{my_password}@localhost/backend_project"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 