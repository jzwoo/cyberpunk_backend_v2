from pydantic import BaseModel


class Cart(BaseModel):
    username: str
    likes: list[str] = []
    cart: list[str] = []
