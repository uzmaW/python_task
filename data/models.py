from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey 
from datetime import datetime
from sqlalchemy.orm import relationship
from typing import Optional





Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    first_name = Column(String)
    last_name = Column(String)
    # phone = Column(String)
    # address = Column(String)
    # city = Column(String)
    # state = Column(String)
    # zip = Column(String)
    # country = Column(String)
    profile_picture = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
   # todos = relationship("Todo", back_populates="owner")


    
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True,nullable=True)
    is_done = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="pending")
    owner_id:Optional[Integer] = Column(Integer, ForeignKey("users.id"), index=True, default=None,nullable=True)
    #owner = relationship("User", back_populates="todos")
    updated_at:Optional[DateTime] = Column(DateTime, default=None, nullable=True)
    deleted_at:Optional[DateTime] = Column(DateTime, default=None, nullable=True)
    deleted_by:Optional[Integer] = Column(Integer, default=None, nullable=True)
    completed_by:Optional[Integer] = Column(Integer, default=None, nullable=True)
    completed_at:Optional[DateTime] = Column(DateTime, default=None, nullable=True)

    

# class User_Todos:
#     id= Column(Integer, primary_key=True, index=True)
#     user_id = relationship("User", back_populates="user_id")
#     todos_id = relationship("Todo", back_populates="todos_id")

class JwtToken(Base):
    __tablename__ = "jwt_tokens"

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String, index=True)
    user_id = Column(Integer, index=True)

class Logger(Base):
    __tablename__ = "system_log"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    action = Column(String, index=True)
    time = Column(String, index=True)
    ip = Column(String, index=True)
    data = Column(String, index=True)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_done = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)