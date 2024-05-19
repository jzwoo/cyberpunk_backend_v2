from pydantic import BaseModel

from common.models.uuid import UUID


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
