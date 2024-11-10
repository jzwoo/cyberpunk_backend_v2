from typing import Annotated

from fastapi import APIRouter, HTTPException, Body, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import ValidationError

from db.db import get_db
from microservices.user_svc.controllers.auth.github import get_user_details
from microservices.user_svc.controllers.auth.google import verify_id_token
from microservices.user_svc.dal.user_DAL import UserDAL
from microservices.user_svc.models.user import (
    LoginSuccessResponse,
    UserIn,
    Identity,
    UserOut,
)
from microservices.user_svc.utils.jwt_utils import (
    generate_access_token,
    generate_refresh_token,
    decode_access_token,
    decode_refresh_token,
)

auth = APIRouter()

user_dal = UserDAL(db=get_db())

auth_scheme = HTTPBearer()

tags = ["Auth"]


@auth.post(
    "/api/v1/auth/{provider}-login",
    response_description="Social login",
    response_model=LoginSuccessResponse,
    tags=tags,
)
async def social_login(provider: str, token: Annotated[str, Body(embed=True)]):
    if provider == "google":
        id_info = await verify_id_token(token)

        user_email = id_info.get("email")
        user_name = id_info.get("name")
        user_id = id_info.get("sub")
    elif provider == "github":
        user_details = await get_user_details(token)

        user_email = user_details.get("email")
        user_name = user_details.get("name")
        user_id = user_details.get("id")
    else:
        raise HTTPException(status_code=400, detail="Unsupported provider")

    identity = Identity(provider=provider, user_id=user_id, name=user_name)

    if (existing_user := await user_dal.get_user_by_email(email=user_email)) is None:
        new_user = UserIn(name=user_name, email=user_email, identities=[identity])

        user = UserOut(**await user_dal.create_user(new_user))
    else:
        curr_user = UserIn(**existing_user)
        curr_user.name = user_name

        if not curr_user.has_identity(provider):
            curr_user.identities.append(identity)

        user = UserOut(**await user_dal.update_user(curr_user, user_email))

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    # set refresh token
    await user_dal.set_user_refresh_token(email=user_email, refresh_token=refresh_token)

    return LoginSuccessResponse(
        user=user, access_token=access_token, refresh_token=refresh_token
    )


@auth.post("/api/v1/auth/logout", response_description="Logout", tags=tags)
async def logout(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    try:
        requester = decode_access_token(credentials.credentials)
    except ValidationError:
        raise HTTPException(status_code=401, detail="Invalid token")

    await user_dal.unset_user_refresh_token(requester.email)


@auth.post(
    "/api/v1/auth/refresh",
    response_description="Refresh Token",
    response_model=LoginSuccessResponse,
    tags=tags,
)
async def refresh(
    refresh_token: Annotated[str, Body(embed=True)],
):
    try:
        requester = decode_refresh_token(refresh_token)
    except ValidationError:
        raise HTTPException(status_code=401, detail="Invalid token")

    if (existing_user := await user_dal.get_user_by_email(requester.email)) is None:
        raise HTTPException(status_code=403)

    user = UserOut(**existing_user)

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    # set refresh token
    await user_dal.set_user_refresh_token(email=user.email, refresh_token=refresh_token)

    return LoginSuccessResponse(
        user=user, access_token=access_token, refresh_token=refresh_token
    )
