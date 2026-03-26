from pydantic import BaseModel, Field
from typing import Optional

class NombrePais(BaseModel):
    common: str = Field(default="N/A")
    official: str = Field(default="N/A")

class CapitalInfo(BaseModel):
    latlng: list[float] = Field(default_factory=list)

class PaisModel(BaseModel):
    name: NombrePais
    capital: list[str] = Field(default_factory=lambda: ["N/A"])
    region: str = Field(default="N/A")
    subregion: str = Field(default="N/A")
    maps: dict = Field(default_factory=lambda: {"googleMaps": "N/A"})
    cca2: str = Field(default="N/A")
    independent: bool = Field(default=False)
    population: Optional[int] = Field(default=None)
    capitalInfo: CapitalInfo