from pydantic import BaseModel

from common.models.uuid import UUID


class UserIn(BaseModel):
    username: str
    password: str
    name: str


class UserOut(UUID, BaseModel):
    username: str
    name: str


class LoginSuccessResponse(BaseModel):
    user: UserOut
    access_token: str
