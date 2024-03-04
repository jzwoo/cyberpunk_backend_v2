from fastapi import APIRouter, HTTPException

from db.db import get_db
from products.controllers.create_product_controller import create_product_controller
from products.controllers.delete_product_controller import delete_product_controller
from products.controllers.get_product_controller import get_product_controller
from products.controllers.get_products_controller import get_products_controller
from products.dal.product_DAL import ProductDAL
from products.models.product import ProductOut, ProductIn

product = APIRouter()

product_dal = ProductDAL(db=get_db())

tags = ["Product"]


@product.get(
    "/api/v1/products",
    response_description="Get products",
    response_model=list[ProductOut],
    tags=tags,
)
async def get_products():
    return await get_products_controller(product_dal, query=None)


@product.get(
    "/api/v1/products/{product_uuid}",
    response_description="Get product",
    response_model=ProductOut,
    tags=tags,
)
async def get_product(product_uuid: str):
    try:
        return await get_product_controller(product_dal, product_uuid)
    except ValueError as e:
        raise HTTPException(status_code=404, detail="Product is not found.")


@product.post(
    "/api/v1/products",
    response_description="Create product",
    response_model=ProductOut,
    status_code=201,
    tags=tags,
)
async def create_product(new_product: ProductIn):
    return await create_product_controller(product_dal, new_product)


@product.delete(
    "/api/v1/products/{product_uuid}",
    response_description="Delete product",
    status_code=204,
    tags=tags,
)
async def delete_product(product_uuid: str):
    try:
        await delete_product_controller(product_dal, product_uuid)
    except ValueError as e:
        raise HTTPException(status_code=404, detail="Product is not found.")
