from typing import Optional

from pydantic import BaseModel, Field

from fastapi import Body, FastAPI, HTTPException, Path, Query
from fastapi.responses import HTMLResponse

app = FastAPI(
    title='Aprendiendo FastApi',
    description='Una API solo por diversión',
    version='0.1.0',
)


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=15, max_length=35)

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


movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción',
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción',
    },
]


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int = Path(ge=1, le=2000)):
    for item in movies:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Movie not found")


@app.get('/movies/', tags=['movies'])  # Se pone la barra al final de la url para indicar que vamos a recibir parámetros
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    return [movie for movie in movies if movie['category'] == category]


# ----------------------------- Método POST -----------------------------
@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie.model_dump())
    return movies


@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return movies


@app.delete('/movies/{id}', tags=['movies'])
def delete_movies(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies
