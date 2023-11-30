from typing import Optional

from pydantic import BaseModel

from fastapi import Body, FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI(
    title='Aprendiendo FastApi',
    description='Una API solo por diversión',
    version='0.1.0',
)


class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str


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
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Movie not found")


@app.get('/movies/', tags=['movies'])  # Se pone la barra al final de la url para indicar que vamos a recibir parámetros
def get_movies_by_category(category: str):
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
