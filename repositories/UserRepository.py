from typing import Any, List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from data.models import User
from database import get_db 

class UserRepository:
    db: Session

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.db: Session = Depends(get_db)
    
    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[User]:
        query = self.db.query(User)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()
        
    @classmethod
    def get_by_id(self, user_id: int, db)->User|None:
        return db.query(User).filter(User.id == user_id).first() or None

