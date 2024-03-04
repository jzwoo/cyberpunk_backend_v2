import uuid
from pydantic import BaseModel, Field


class UUID(BaseModel):
    uuid: str = Field(default_factory=uuid.uuid4)