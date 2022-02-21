from datetime import datetime
from typing import List
from sqlalchemy.orm.session import Session
from db.database import Base
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username = str 
    email = str

    class Config():
        orm_mode=True


class PostBase(BaseModel):
    img_url: str 
    img_url_type : str 
    caption: str 
    creator_id: int

#For PostDisplay   

class User(BaseModel):
    username: str
    class Config():
        orm_mode=True

#For PostDisplay

class Comment(BaseModel):
    text: str 
    username: str 
    timestamp: datetime 
    class Config():
        orm_mode=True




class PostDisplay(BaseModel):
    id: int 
    img_url: str 
    img_url_type: str 
    caption: str 
    timestamp: datetime
    user: User
    comments: List[Comment]
    class Config():
        orm_mode=True


class UserAuth(BaseModel):
    id: int 
    username: str 
    email: str

class CommentBase(BaseModel):
    username: str 
    text:str 
    post_id: int 