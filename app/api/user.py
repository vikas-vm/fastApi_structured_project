from fastapi import APIRouter, Depends, HTTPException
from app.services import user_service, item_service
from app.schemas import user_schema, item_schema
from sqlalchemy.orm import Session

from app.dependencies import get_db

user_router = APIRouter()


@user_router.post("/", response_model=user_schema.UserSchema)
async def create_user(user: user_schema.UserCreateSchema, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(db=db, user=user)


@user_router.get("/", response_model=list[user_schema.UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_service.get_users(db, skip=skip, limit=limit)
    return users


@user_router.get("/{user_id}", response_model=user_schema.UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@user_router.post("/{user_id}/items/", response_model=item_schema.ItemSchema)
def create_item_for_user(
    user_id: int, item: item_schema.ItemCreateSchema, db: Session = Depends(get_db)
):
    return item_service.create_user_item(db=db, item=item, user_id=user_id)
