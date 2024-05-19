import jwt
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import ValidationError

from microservices.cart_svc.controllers.create_or_get_cart_controller import (
    create_or_get_cart_controller,
)
from microservices.cart_svc.dal.cart_DAL import CartDAL
from microservices.cart_svc.models.cart import Cart
from db.db import get_db
from microservices.user_svc.utils.jwt_utils import decode_access_token

cart = APIRouter()

cart_dal = CartDAL(db=get_db())

auth_scheme = HTTPBearer()

tags = ["Cart"]


@cart.get(
    "/api/v1/carts/{username}",
    response_description="Get cart",
    response_model=Cart,
    tags=tags,
)
async def get_cart(
    username: str, credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)
):
    try:
        requester = decode_access_token(credentials.credentials)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except ValidationError:
        raise HTTPException(status_code=401, detail="Invalid token")

    if requester.username != username:
        raise HTTPException(status_code=403)

    return await create_or_get_cart_controller(cart_dal, username)
