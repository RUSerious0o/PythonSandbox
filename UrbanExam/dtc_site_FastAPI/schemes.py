from pydantic import BaseModel


class User(BaseModel):
    username: str
    disabled: bool | None = False