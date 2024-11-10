from pydantic import BaseModel, EmailStr

from common.models.id import Id


class Identity(BaseModel):
    provider: str
    user_id: int | str
    name: str


class UserIn(BaseModel):
    name: str
    email: EmailStr
    identities: list[Identity] = []

    def has_identity(self, provider: str):
        for identity in self.identities:
            if provider == identity.provider:
                return True

        return False


class UserOut(Id, UserIn):
    pass


class LoginSuccessResponse(BaseModel):
    user: UserOut
    access_token: str
    refresh_token: str
