from pydantic import BaseModel


class TokenIn(BaseModel):
    uuid: str
    username: str
