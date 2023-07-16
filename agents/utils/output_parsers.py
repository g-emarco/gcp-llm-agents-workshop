from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class SearchResponse(BaseModel):
    answer: str = Field(description="summary of answer derived from google")
    torq_count: int = Field(description="number of times the word torq was mentioned in the answer")


parser = PydanticOutputParser(pydantic_object=SearchResponse)
