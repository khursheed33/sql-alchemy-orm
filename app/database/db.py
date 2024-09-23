from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

class Database:
    def __init__(self) -> None:
        self.Base:Engine  = declarative_base()
        self.DATABASE_URL = "sqlite:///./test.db"
        
    def engine(self) -> Engine:
        return create_engine(self.DATABASE_URL, echo=True)

    def session(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine())
    
    def get_database(self) -> Session:
        db = self.session()
        try:
            yield db
        finally:
            db.close()
