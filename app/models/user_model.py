from database.db import Database
from sqlalchemy import Column, Integer, String, Sequence

db = Database()

class User(db.Base):
    __tablename__ = "users"
    
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(length=100), nullable=False)
    surname = Column(String(length=100), nullable=False)
    email = Column(String(length=100), nullable=False)
    
    def __repr__(self) -> str:
        return """
    <User(
        id='%s', 
        name='%s', 
        name='%s', surname='%s',
        email='%s', surname='%s'
        )
        >" % (self.id, self.name, self.surname, self.email,)>"""
        


