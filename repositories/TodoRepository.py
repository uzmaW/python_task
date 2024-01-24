from typing import List, Optional, Any
from fastapi import Depends
from sqlalchemy.orm import Session
from data.models import Todo
from database import get_db 
from data.schemas import TodoCreate
from fastapi import HTTPException


class TodoRepository:
    db: Session

    def __init__(
        self, db: Session
    ) -> None:
        self.db = db
    def setDb(self,db):
        self.db = db
        return self

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Todo]:
        query = self.db.query(Todo)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()
    
    def get(self, todo_id: int) -> Any | Todo:
        todo =self.db.query(Todo).filter(Todo.id==todo_id).first() or None
        if todo is None:
           raise HTTPException(status_code=404, detail="Todo not found")
        return todo 
    
    def create(self, todo_create: TodoCreate) -> Todo:
        db_item = Todo(**todo_create.dict())
        self.db.add(self.db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
    
def get_todo_repository(db):
    return TodoRepository(db)    