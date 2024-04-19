from pydantic import BaseModel


class ItemBaseSchema(BaseModel):
    title: str
    description: str | None = None


class ItemCreateSchema(ItemBaseSchema):
    pass


class ItemSchema(ItemBaseSchema):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
