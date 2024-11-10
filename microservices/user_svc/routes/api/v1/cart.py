from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBearer

from db.db import get_db
from microservices.user_svc.dal.cart_DAL import CartDAL
from microservices.user_svc.models.cart import Cart
from microservices.user_svc.routes.api.v1.auth import user_dal

cart = APIRouter()

cart_dal = CartDAL(db=get_db())

auth_scheme = HTTPBearer()

tags = ["Cart"]


@cart.get(
    "/api/v1/users/{user_id}/cart",
    response_description="Retrieve or create user's cart",
    response_model=Cart,
    tags=tags,
)
async def get_cart(user_id: str):
    if await user_dal.get_user_by_id(user_id=user_id) is None:
        raise HTTPException(status_code=404)

    if (user_cart := await cart_dal.get_cart(user_id=user_id)) is None:
        user_cart = await cart_dal.create_cart(cart=Cart(user_id=user_id))

    return user_cart


@cart.put(
    "/api/v1/users/{user_id}/cart",
    response_description="Create or update user's cart",
    response_model=Cart,
    tags=tags,
)
async def update_or_create_cart(user_id: str, updates: Cart):
    if await user_dal.get_user_by_id(user_id=user_id) is None:
        raise HTTPException(status_code=404)

    updates.user_id = user_id

    if await cart_dal.get_cart(user_id=user_id) is None:
        return await cart_dal.create_cart(cart=updates)
    else:
        return await cart_dal.update_cart(user_id=user_id, updated_cart=updates)
