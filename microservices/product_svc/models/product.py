from pydantic import BaseModel

from common.models.id import Id


class ProductImage(BaseModel):
    url: str
    aspectRatio: float


class ProductIn(BaseModel):
    name: str
    description: str
    image: ProductImage
    price: int
    quantity: int


class ProductOut(Id, ProductIn):
    pass
