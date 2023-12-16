from typing import List

from fastapi import APIRouter, HTTPException, Path, Query, status
from fastapi.responses import HTMLResponse, JSONResponse
from models.movies import Movie
from utils.loads import load_json_data

router = APIRouter()


@router.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')


@router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies():
    return JSONResponse(
        status_code=200, content=load_json_data()
    )  # Este status code no es necesario porque ya se añadió en el decorador


@router.get('/movies/{id}', tags=['movies'], status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)):
    movies = load_json_data()

    for item in movies:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")


@router.get(
    '/movies/', tags=['movies'], status_code=200
)  # Se pone la barra al final de la url para indicar que vamos a recibir parámetros
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    movies = load_json_data()
    return [movie for movie in movies if movie['category'] == category]
