from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./ch4/test.db"
engine = create_engine(DATABASE_URL, echo=True)