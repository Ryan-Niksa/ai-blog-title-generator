from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from .deps import get_db

router = APIRouter()

@router.post("/posts", response_model=schemas.BlogPostOut)
def create_post(post: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)

@router.get("/posts", response_model=list[schemas.BlogPostOut])
def list_posts(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.get_posts(db, skip, limit)

@router.get("/posts/{post_id}", response_model=schemas.BlogPostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/posts/{post_id}", response_model=schemas.BlogPostOut)
def update_post(post_id: int, update: schemas.BlogPostUpdate, db: Session = Depends(get_db)):
    post = crud.update_post(db, post_id, update)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_post(db, post_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"status": "deleted"}
