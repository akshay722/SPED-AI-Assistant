from pydantic import BaseModel
from fastapi import Query, Body


class scrapeData(BaseModel):
    contentType: str = Body(embed=True)
    name: str = Body(embed=True)
    fileContent: str = Body(embed=True)  # Optional[]
    # sessionId: str = Query()
    # userId: str = Query()


class createSession(BaseModel):
    userId: str = Body(embed=True)


class updateSession(BaseModel):
    sessionName: str = Body(embed=True)


class DeleteVector(BaseModel):
    userId: str = Query(...)
    sessionId: str = Query(...)
