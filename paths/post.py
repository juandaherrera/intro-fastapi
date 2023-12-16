import json

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse
from models.movies import Movie
from utils.loads import json_path, load_json_data

router = APIRouter()


@router.post('/movies', tags=['movies'], status_code=201)
def create_movie(movie: Movie):
    movies = load_json_data()

    movies.append(movie.model_dump())

    with open(json_path, 'w') as file:
        json.dump(movies, file, indent=4)
    return movies
