from datetime import datetime

from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    id: str
    email: EmailStr
    name: str
    iss: str
    iat: datetime
    exp: datetime
