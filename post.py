import random, string, shutil

from typing import List
from auth.auth2 import get_current_user
from fastapi import APIRouter, Depends , status, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from routers.schemas import PostBase, PostDisplay
from db.database import get_db
from db import db_post
from routers.schemas import UserAuth

router = APIRouter(
    prefix="/post",
    tags=["post"]
)

img_url_types = ["absolute", "relative"]


@router.post("", response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    """
    Create post
    
    - This path operation creates a new post in the app and save the infomation in the database

    ***Important Note***

    - To use you need a access token 

    ***Parameters***:
        
    - Request body parameter:

    - **post: Post** -> A post model with  img_url, img_url_type (you can choose between absolute or relative), caption and the creator_id (its be equal at the user in session)
    
    **Note about img_url_type**

    - When use a values?
    - **absolute** when the url type from another website
    - **relative** when you use a /post/image and this route return a realtive route like *img/imagename.jpg*

    """

    if not request.img_url_type in img_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
         default="Parameter img_url_type can only takes values absolute oṛ relative ")
    return db_post.create(db, request)

@router.get("/all", response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    """
    Posts

    - This path operation show all posts created in the app with all info and comments about them


    Parameters

    - You dont need logged for wacth something *We will change that some day*

    Return 

    - All post

    """
    return db_post.get_all(db)

@router.post("/image")
def upload_image(image: UploadFile =File(...), current_user: UserAuth = Depends(get_current_user)):

    """
    Upload Image

    - This path operation generates a relative path for storage img in our own server

    Parameters

    - its a **multipart/form-data** so look how integrate this in your front xd

    Returns

    - A relative path where the image was saved

    """
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for i in range(6))
    new = f"_{rand_str}."
    filename = new.join(image.filename.rsplit('.', 1))
    path = f"img/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}

@router.get("/delete/{id}")
def delete(id: int, db: Session = Depends(get_db), current_user: UserAuth= Depends(get_current_user)):
    """
    Delete Post

    - This path operation deleted a post

    Parameters

    - id its a value from a identifier from that post
    - only the current user can delete own creations 

    Return 
    
    -Succesful string XD
    """
    return db_post.delete(db, id, current_user.id)