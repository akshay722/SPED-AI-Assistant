from pydantic import BaseModel
from fastapi import Query


class User(BaseModel):
    sessionId: str = Query()
    userId: str = Query()
