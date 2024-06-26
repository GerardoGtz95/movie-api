from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None;
    #  title: str = Field(default="Mi pelicula", min_length=5 ,max_length=15)
    title: str = Field(min_length=5 ,max_length=50)
    overview: str = Field(min_length=15 ,max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)
    
    # Para valores por defecto y evitar el parametro default en Fields
    class Config:
        schema_extra = {
          "example": {
            "id": 1,
            "title": 'Mi pelicula',
            "overview": "Descripción de la pelicula",
            "year": 2022,
            'rating': 9.8,
            "category": "Action"
          }
        }