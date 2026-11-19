import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# DATABASE_URL=mysql+pymysql://usuario:senha@servidor:3306/banco
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///atividade.db")
Base = declarative_base()
engine = create_engine(DATABASE_URL)
