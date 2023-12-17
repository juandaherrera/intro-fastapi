from typing import Optional

from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=30)
    overview: str = Field(min_length=10, max_length=80)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=20)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Mi Pelicula",
                    "overview": "Descripcion de la pelicula",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción",
                }
            ]
        }
    }
