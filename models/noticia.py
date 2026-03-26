from pydantic import BaseModel, Field
from typing import Optional

class NoticiasModel(BaseModel):
    title: str = Field(default="N/A")
    description: Optional[str] = Field(default=None)
    pubDate: str = Field(default="N/A")
    video_url: Optional[str] = Field(default=None)
