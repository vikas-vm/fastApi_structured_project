from fastapi import APIRouter, Depends, HTTPException
from app.services import item_service
from app.schemas import item_schema
from sqlalchemy.orm import Session

from app.dependencies import get_db

item_router = APIRouter()


@item_router.get("/", response_model=list[item_schema.ItemSchema])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item_service.get_items(db, skip=skip, limit=limit)
    return items
