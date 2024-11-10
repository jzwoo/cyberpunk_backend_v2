from datetime import datetime

from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    id: str
    email: EmailStr
    name: str
    iat: datetime
    exp: datetime
