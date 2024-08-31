from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

# DB Connection
# DATABASE_URL = "postgresql+psycopg2://postgres:mach1029@localhost/DogsAPI_DB"
# DATABASE_URL = "mysql+pymysql://username:password@localhost/dbname"
DATABASE_URL = "sqlite:///DogsAPI_DB.db"

# DB Configuration with ORM
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()