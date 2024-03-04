from fastapi import APIRouter

from db.db import get_db
from products.dal.product_DAL import ProductDAL
from products.models.product import ProductOut

product = APIRouter()

product_dal = ProductDAL(db=get_db())


@product.get(
    "/api/v1/products",
    response_description="Get all products",
    response_model=list[ProductOut],
)
async def get_products():
    return await product_dal.get_products()
