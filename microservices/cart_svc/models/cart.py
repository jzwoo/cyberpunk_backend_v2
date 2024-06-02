from pydantic import BaseModel


class Cart(BaseModel):
    provider: str
    user_id: str
    likes: list[str] = []
    cart: list[str] = []
