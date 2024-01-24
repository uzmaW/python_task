
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List 
from repositories.UserRepository import UserRepository
from data.schemas import User,UserBasic
from database import get_db


router = APIRouter(prefix="/users", tags=["user"])

def get_user_repository(
    ) -> UserRepository:
    return UserRepository()
        

class User:
        
    @router.get("/{user_id}", response_model=UserBasic)
    def get_user(user_id: int, user_repository: UserRepository=Depends(get_user_repository), db:Session=Depends(get_db)) -> User:
        
        user = user_repository.get_by_id(user_id, db)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
        
    
    @router.post("/{id}")
    def delete_user(id: int)->dict:
        return {"id": id, "title": "Todo " + str(id)} or None

    @router.get("/", response_model=List[User])
    def get_users():
        return {"message":"todos"}
    
    @router.post("/")
    def create_user():
        return {"message":"todo created"}
    
    @router.put("/{id}")
    def update_user():
        return {"message":"todo updated"}
    
    @router.delete("/{id}")
    def delete_user():
        return {"message":"todo deleted"}
    
