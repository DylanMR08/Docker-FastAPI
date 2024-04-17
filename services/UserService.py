from typing import Optional, List
from sqlalchemy.orm import Session
from database.database import SessionLocal
from model import User as User

class UserService:
    
    __db = SessionLocal()
    
    @classmethod
    def create_user(cls, user_data: dict) -> User:
        user = User(**user_data)
        cls.__db.add(user)
        cls.__db.commit()
        cls.__db.refresh(user)
        return user

    @classmethod
    def get_user(cls, user_id: int) -> User | None:
        return cls.__db.query(User).filter(User.id == user_id).first()

    @classmethod
    def update_user(cls,user_id: int, user_data: dict) -> User | None:
        user = cls.__db.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            cls.__db.commit()
            cls.__db.refresh(user)
        return user

    @classmethod
    def delete_user(cls, user_id: int) -> bool:
        user = cls.__db.query(User).filter(User.id == user_id).first()
        if user:
            cls.__db.delete(user)
            cls.__db.commit()
            return True
        return False
