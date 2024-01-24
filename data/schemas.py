from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, date
from typing import Optional, Union




# class User(BaseModel):
#     name : str
#     email: str
#     password: str



# User schemas
class UserBase(BaseModel):
    id: int
    is_active: bool
   
class UserBasic(UserBase):
   # firstname: str
   # lastname: str
    email: str
    
       
class User(UserBase):
    firstname: str = Field(
        title="The name of the User to do",
        description="The name has a maximum length of 50 characters",
        max_length=50,
        example = "John doe"
    )
    lastname: str = Field(
        title="The name of the User to do",
        description="The name has a maximum length of 50 characters",
        max_length=50,
        example = "John doe"
    )
    email : str = Field(
        title="The email of the user",
        description="The email has a maximum length of 50 characters",
        max_length=50,
        example = "user@gmail.com"
    )
    # password: str
    created_at : Optional[date] = None
    updated_at : Optional[date] = None

class UserCreate(User):
    password: str

class TodoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title : str = Field(
        title="The title of the todo",
        description="The title has a maximum length of 50 characters",
        max_length=50,
        example = "Buy milk"
    )
    description : str = Field(
        title="The description of the todo",
        description="The description has a maximum length of 50 characters",
        max_length=50,
        example = "Buy milk from the store"
        # default="Buy milk from the store"
        )
    is_done: bool = Field(
        title="The status of the todo",
        description="The status has a maximum length of 50 characters",
        example = False
    )
    
    status: Optional[str] = Field(
        title="The status of the todo",
        max_length=50,
        example="pending"
    )
    created_at : Optional[datetime] = None
  
    owner_id: Optional[int] = Field(
        title="The user id of the todo",
        example=1
    )
 


class TodoCreate(TodoBase):
    # model_config = ConfigDict(from_attributes=True)
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    deleted_at: Optional[datetime] = Field(default=None, alias="deletedAt")
    deleted_by: Optional[int] = Field(default=None, alias="deletedBy")
    completed_by: Optional[int] = Field(default=None, alias="completedBy")
    completed_at: Optional[datetime] = Field(default=None, alias="completedAt")  # Optional[int] = Field(default=None, alias="completedBy")  # Optional[int] = Field(default=None, alias="completedBy")  # Optional[int] = Field(default=None, alias="completedBy


#     class Config():
#         from_attributes=True
class TodoOut(TodoBase):
    id: int
    is_done: Optional[bool] = False
# class TodoDTO(BaseModel):
#     # id : int
#     title : str
#     description : str
#     user_id : int
#     created_at : Optional[date] = None
#     is_done: Optional[str] = None

#     class Config():
#         from_attributes = True


class TodoUpdate(TodoBase):
    title : Optional[str] = None
    description : Optional[str] = None
    updated_at : Optional[date] = None
    is_done: Optional[str] = None

#     class Config():
#         from_attributes = True

    
    
# class Login(BaseModel):
#     email: str
#     password: str


# class Token(BaseModel):
#     access_token: str
#     user_id: int

#     class Config():
#         from_attributes = True

class TaskBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title : str = Field(
        title="The title of the task",
        description="The title has a maximum length of 50 characters",
        max_length=50,
        example = "Buy milk"
    )
    description : str = Field(
        title="The description of the task",
        description="The description has a maximum length of 50 characters",
        max_length=50,
        example = "Buy milk from the store"
    )
    is_done : bool = Field(
        title="The status of the task",
        description="The status has a maximum length of 50 characters",
        example = False
    )
    created_at : Optional[datetime] = None
    owner_id: Optional[int] = Field(
        title="The user id of the task",
        example=1
    )

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    is_done: Optional[bool] = False
    description: Optional[str] = None
    title: Optional[str] = None
