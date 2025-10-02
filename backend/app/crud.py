from sqlalchemy.orm import Session
from . import models, schemas

def create_post(db: Session, post: schemas.BlogPostCreate):
    db_post = models.BlogPost(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip=0, limit=50):
    return db.query(models.BlogPost).offset(skip).limit(limit).all()

def get_post(db: Session, post_id: int):
    return db.query(models.BlogPost).filter(models.BlogPost.id == post_id).first()

def update_post(db: Session, post_id: int, update: schemas.BlogPostUpdate):
    post = get_post(db, post_id)
    if not post:
        return None
    for key, value in update.dict(exclude_unset=True).items():
        setattr(post, key, value)
    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = get_post(db, post_id)
    if not post:
        return None
    db.delete(post)
    db.commit()
    return post
