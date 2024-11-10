from pydantic import BaseModel


class Cart(BaseModel):
    user_id: str
    likes: list[str] = []
    items: list[str] = []
