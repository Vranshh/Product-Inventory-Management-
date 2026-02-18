from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:100987@localhost:5432/telusko"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush=False, bind=engine)