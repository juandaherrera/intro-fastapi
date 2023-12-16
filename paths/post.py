import json

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse
from models.movies import Movie
from models.users import User
from utils.jwt_manager import create_token
from utils.loads import json_path, load_json_data

router = APIRouter()


@router.post('/movies', tags=['movies'], status_code=201)
def create_movie(movie: Movie):
    movies = load_json_data()

    movies.append(movie.model_dump())

    with open(json_path, 'w') as file:
        json.dump(movies, file, indent=4)
    return movies


@router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token: str = create_token(
            user.model_dump()
        )  # Hay que tener cuidado con lo que se pone en el payload, esto lo puede ver cualquiera con un debugger: https://jwt.io/
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=401, content={"message": "Credenciales inválidas, intente de nuevo"})
