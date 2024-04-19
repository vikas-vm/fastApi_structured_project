from pydantic import BaseModel
from .item_schema import ItemSchema


class UserBaseSchema(BaseModel):
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int
    is_active: bool
    items: list[ItemSchema] = []

    class Config:
        from_attributes = True
