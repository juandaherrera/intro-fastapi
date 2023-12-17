from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Column, Float, Integer, String

from config.database import Base


# Si queremos tener un solo modelo para Bd y validaciones, podemos usar SQLModel de tiangolo
class MovieBD(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)


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
                    "id": 1,
                    "title": "Mi Pelicula",
                    "overview": "Descripcion de la pelicula",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción",
                }
            ]
        }
    }
