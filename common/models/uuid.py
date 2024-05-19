from pydantic import BaseModel


class UUID(BaseModel):
    uuid: str
