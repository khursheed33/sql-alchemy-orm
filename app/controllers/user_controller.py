from sqlalchemy.orm import Session
from app.database.db import Database
from app.models.user_model import User


class UserController(Database):
    def __init__(self) -> None:
        super().__init__()
        self.db = self.get_database()
    # Function to create a new user
    def create_user(self, user: User):
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    # Function to get a user by name (example)
    def get_user_by_name(db: Session, name: str):
        return self.db.query(User).filter(User.name == name).first()

    # Function to get all users (example)
    def get_users(db: Session, skip: int = 0, limit: int = 10):
        return self.db.query(User).offset(skip).limit(limit).all()
