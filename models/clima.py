from pydantic import BaseModel, Field
from typing import Optional

class ClimaCurrent(BaseModel):
    temperature_2m: Optional[float] = Field(default=None)
    weathercode: int = Field(default=0)

class ClimaModel(BaseModel):
    current: ClimaCurrent