from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from settings import Settings as settings

from data.models import User,Todo,JwtToken,Logger,Base
from sqlalchemy import inspect
#import psycopg2
#from psycopg2.extras import RealDictCursor
#import inspect
from sqlalchemy import event
from security.crypto import pwd_context

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
# Check if the database exists

#inspector = inspect(engine)
#database_exists = inspector.engine.dialect.has_database(engine, settings.SQLALCHEMY_DATABASE_URI)
# if not database_exists:
#     database_name = settings.SQLALCHEMY_DATABASE_URI.split("/")[-1]
#     engine.execute(f"CREATE DATABASE {database_name}")
#     print(f"Database {database_name} created successfully.")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def seed_tables(target, connection, **kw):
    """if database is seeded then exit
    Args:
        target (_type_): _description_
        connection (_type_): _description_
    """
    if(connection.scalar(User.__table__.select().where(User.email == 'admin@example.com'))):
        return
    connection.execute(User.__table__.insert(), [
        {
            'email': 'admin@example.com',
            'hashed_password': pwd_context.hash('admin123'),
            'is_superuser': True
        }
    ])
    connection.execute(Todo.__table__.insert(), [
        {
            'title': 'Todo 1',
            'description': 'Description 1',
            'owner_id': 1
        },
        {
            'title': 'Todo 2',
            'description': 'Description 2',
            'owner_id': 1
        },
        {
            'title': 'Todo 3',
            'description': 'Description 3',
            'owner_id': 1
        }
    ])

event.listen(Todo.__table__, 'after_create', seed_tables)


    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def create_tables(engine):
    Base.metadata.create_all(bind=engine)

def drop_tables(engine):
    Base.metadata.drop_all(bind=engine)

def setup_database(db:Session):
    try:        
        create_tables(engine)
        # add default user
     
    except Exception as e:
        print(e)
    
     