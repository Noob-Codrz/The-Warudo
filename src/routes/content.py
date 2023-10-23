from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.schemas import ContentBase
from models.models import Content, Comment_comment, Content_comment, Comments
from database.database import get_db

router = APIRouter()

@router.get("/{content_id}")
async def get_content(content_id: int, db: Session = Depends(get_db)):
    return db.query(Content).filter(Content.id == content_id).first()

@router.post("/")
async def create_content(content: ContentBase, db: Session = Depends(get_db)):
    db_content = Content(**content.dict())
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content

@router.put("/{content_id}")
async def update_content(content_id: int, content: ContentBase, db: Session = Depends(get_db)):
    db_content = db.query(Content).filter(Content.id == content_id).first()
    update_content = content.model_dump(exclude_unset=True)
    for key, value in update_content.items():
        setattr(db_content, key, value)
    db.commit()
    db.refresh(db_content)
    return db_content

@router.get("/{content_id}/comments")
async def get_comments(content_id: int, db: Session = Depends(get_db)):
    return db.query(Content).filter(Content.id == content_id).first().comments

#nested comments later
    