
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from data.schemas import TodoCreate,TodoUpdate, TodoBase, TodoOut
from data.models import Todo
from repositories.TodoRepository import get_todo_repository
from typing import Optional,Any

from sqlalchemy.orm import Session
from database import get_db


router = APIRouter(prefix="/todos", tags=["todo"])

class Todos: 
    @router.get("/{id}", response_model=TodoOut)
    def get_todo(todo_id: int, db: Session=Depends(get_db)) -> Any: #TodoBase:
        return get_todo_repository(db).get(todo_id)
        
    
    @router.get("/", response_model=List[TodoOut])
    def get_todos(
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
        db: Session = Depends(get_db)
    ) -> List[TodoOut]:
         return get_todo_repository(db).list(limit, offset)
        
    @router.post("/add", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
    def create_todo(todo: TodoCreate, db:Session=Depends(get_db)):
        return get_todo_repository(db).get(todo)

        
    @router.put("/{id}")
    def update_todo(todo: TodoUpdate, db: Session=Depends(get_db)):
        return get_todo_repository(db).update(todo)
    
    @router.delete("/{id}")
    def delete_todo(todo_id: int, db:Session=Depends(get_db)):
        return get_todo_repository(db).delete(todo_id)

    
