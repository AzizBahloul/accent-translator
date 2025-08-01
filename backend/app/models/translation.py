from pydantic import BaseModel, Field
from typing import Optional

class TranslationRequest(BaseModel):
    comment: str = Field(..., max_length=500, description="Comment to be translated")
    dialect: str = Field(..., max_length=50, description="Target dialect for translation")
    context: Optional[str] = Field("", max_length=200, description="Optional context for translation")

class TranslationResponse(BaseModel):
    translated_comment: str
