from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, description="The user's travel related question")


class QueryResponse(BaseModel):
    response:str = Field(..., description="LLM generated response")

