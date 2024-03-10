from pydantic import BaseModel

from models.common import UUID


class UserIn(BaseModel):
    username: str
    password: str


class UserOut(UUID, UserIn):
    pass
