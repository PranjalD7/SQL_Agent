from pydantic import BaseModel, Field
from typing import Optional



#pydantic class to generate final answer in a structured format
class SubmitFinalAnswer(BaseModel):
    """Submit the final answer to the user based on the query results."""

    final_answer: str = Field(..., description="The final answer to the user")
