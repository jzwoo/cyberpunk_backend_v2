from pydantic import BaseModel

from common.models.id import Id


class UserIn(BaseModel):
    username: str
    password: str
    name: str


class UserOut(Id, BaseModel):
    username: str
    name: str


class LoginSuccessResponse(BaseModel):
    user: UserOut
    access_token: str
