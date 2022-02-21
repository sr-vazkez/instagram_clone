from auth.auth2 import get_current_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from db.database import get_db
from db import db_comment
from routers.schemas import CommentBase, UserAuth

router= APIRouter(
    prefix="/comment",
    tags=["Comments"]
)

@router.get("/all/{post_id}")
def comments(post_id:int, db: Session = Depends(get_db)):
    """
    COMMENTS

    -This path operathion is for watch all comments for a post
    
    Parameters 

    - Post Id to wacth all comments

    Return 

    - All comments for a specifyc post
    """
    return db_comment.get_all(db, post_id)


@router.post('')
def create(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    """
    Create a Comment

    - This path opreation creates a new comment in a specify post

    Parameters:

    - You can insert a username for a comment
    - add some text
    - and finally the post id where the comment is added

    Returns a string xd

    
    """
    return db_comment.create(db, request) 