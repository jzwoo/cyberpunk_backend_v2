from pydantic import BaseModel

from models.common import UUID


class UserIn(BaseModel):
    username: str
    password: str
    name: str


class UserOut(UUID, BaseModel):
    name: str


class LoginSuccessResponse(BaseModel):
    user: UserOut
    access_token: str
