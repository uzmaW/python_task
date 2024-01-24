from fastapi import FastAPI
import uvicorn
from settings import Settings as settings
import logging
from controllers.User import router as user_router
from controllers.Todos import router as todos_router
from controllers.TokenManager import router as token_manager_router
from database import setup_database,get_db
#from fastapi.middleware.cors import CORSMiddleware
from data.schemas import TaskBase, TaskOut
from data.models import Task
from typing import Any
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
app: FastAPI = FastAPI()

app.title = settings.APP_NAME
app.description = settings.APP_DESCRIPTION
app.version = settings.APP_VERSION
app.debug = settings.DEBUG
#app.docs_url = settings.DOCS_URL

# prepare database
setup_database(get_db)

app.include_router(user_router)
app.include_router(todos_router)
app.include_router(token_manager_router)

@app.get("/")
def index():
    return {"message": "FastAPI : Todo App"}

@app.post("/test", response_model=TaskOut)
def create_task(task_create:TaskBase, db:Session=Depends(get_db))->Any: 
        db_item = Task(**task_create.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item


"""_auto run server from code_"""
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)