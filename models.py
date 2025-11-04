# models.py
from pydantic import BaseModel

class QueryRequest(BaseModel):
    prompt: str

class ToolResponse(BaseModel):
    result: dict
