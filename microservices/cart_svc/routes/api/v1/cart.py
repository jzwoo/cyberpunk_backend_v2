from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from common.providers.providers import SUPPORTED_PROVIDERS
from microservices.cart_svc.controllers.create_or_get_cart_controller import (
    create_or_get_cart_controller,
)
from microservices.cart_svc.controllers.create_or_update_cart_controller import (
    create_or_update_cart_controller,
)
from microservices.cart_svc.dal.cart_DAL import CartDAL
from microservices.cart_svc.models.cart import Cart
from db.db import get_db

cart = APIRouter()

cart_dal = CartDAL(db=get_db())

auth_scheme = HTTPBearer()

tags = ["Cart"]


@cart.get(
    "/api/v1/carts/{user_id}",
    response_description="Get cart",
    response_model=Cart,
    tags=tags,
)
async def get_cart(
    user_id: str,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
):
    if (provider := request.headers.get("X-Provider")) is None:
        raise HTTPException(status_code=400, detail="Provider header is required")

    # get the verify_access_token function for the provider
    if (verify_access_token := SUPPORTED_PROVIDERS.get(provider)) is None:
        raise HTTPException(status_code=400, detail="Invalid provider")

    try:
        await verify_access_token(credentials.credentials)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    return await create_or_get_cart_controller(
        cart_dal, provider=provider, user_id=user_id
    )


@cart.put(
    "/api/v1/carts/{user_id}",
    response_description="Create or update cart",
    response_model=Cart,
    tags=tags,
)
async def update_or_create_cart(
    user_id: str,
    updated_cart: Cart,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
):
    if (provider := request.headers.get("X-Provider")) is None:
        raise HTTPException(status_code=400, detail="Provider header is required")

    # get the verify_access_token function for the provider
    if (verify_access_token := SUPPORTED_PROVIDERS.get(provider)) is None:
        raise HTTPException(status_code=400, detail="Invalid provider")

    try:
        await verify_access_token(credentials.credentials)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    # for create if not exists
    updated_cart.provider = provider
    updated_cart.user_id = user_id

    return await create_or_update_cart_controller(
        cart_dal, provider, user_id, updated_cart
    )
