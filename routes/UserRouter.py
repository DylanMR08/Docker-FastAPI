from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import User as UserSchema
from services import UserService
userRouter = APIRouter(prefix="/user",tags=["Users"])


@userRouter.post("/")
def create_user(data: UserSchema):
    user = UserService.create_user(data.model_dump())
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User created successfully"}

@userRouter.get("/{id}")
def read_user(id: int):
    user = UserService.get_user(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": UserSchema(**user.__dict__).model_dump()}

@userRouter.put("/{id}")
def update_user(id: int, data: UserSchema):
    user = UserService.update_user(id, data.model_dump())
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": UserSchema(**user.__dict__).model_dump()}

@userRouter.delete("/{id}")
def delete_user(id: int):
    deleted = UserService.delete_user(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

