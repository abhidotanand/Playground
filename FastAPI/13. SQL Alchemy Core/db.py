from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./FastAPI/sqlite.db"
engine = create_engine(DATABASE_URL, echo=True)