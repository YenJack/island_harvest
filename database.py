# database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "sqlite")  # "sqlite" or "mysql"
if DB_TYPE == "mysql":
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASS = os.getenv("DB_PASS", "password")
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_NAME = os.getenv("DB_NAME", "harvest")
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
else:
    # sqlite local file
    DATABASE_URL = "sqlite:///./harvest.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DB_TYPE == "sqlite" else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

