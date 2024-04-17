from __future__ import annotations
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(50))
    type_user: Mapped[str] = mapped_column(String(50)) 
    phone: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String(100), unique=True)
    hash_password: Mapped[str] = mapped_column(String(300))

    def __init__(self,**kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.lastname = kwargs.get("lastname")
        self.email = kwargs.get("email")
        self.phone = kwargs.get("phone")
        self.type_user = kwargs.get("type_user")
        self.username = kwargs.get("username")
        self.hash_password = kwargs.get("hash_password")
        
    def __repr__(self) -> str:
        return f"User: <Id: {self.id}, name: {self.name}>"