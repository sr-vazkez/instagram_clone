from sqlalchemy.orm.session import Session
from routers.schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/", response_model=UserDisplay, summary="Create a New User in The app")
def create_user(request: UserBase, db:Session = Depends(get_db)):
    """
    Create User
    
    - This path operation creates a new user in the app and save the infomation in the database

    ***Important Note***

    - IN CASE THAT YOU INTRODUCE A REPEAT EMAIL  OR USERNAME THIS NOT **SAVED** IN DATA BASE

    ***Parameters***:
        
    - Request body parameter:
    - **user: User** -> A user model with  username, email, password

    Return status 202


    """
    return db_user.create_user(db, request)