from pydantic import BaseModel


class SessionCredentials(BaseModel):
    id: str
    token: str
    refresh_token: str
