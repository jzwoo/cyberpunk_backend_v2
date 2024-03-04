from pydantic import BaseModel

from models.common import UUID


class ProductImage(BaseModel):
    url: str
    aspectRatio: float


class ProductIn(BaseModel):
    name: str
    description: str
    image: ProductImage
    price: int
    quantity: int


class ProductOut(UUID, ProductIn):
    pass
