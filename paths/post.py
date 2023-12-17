import json

from config.database import Base, SessionLocal, engine
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse
from models.movies import Movie, MovieBD
from models.users import User
from utils.jwt_manager import create_token
from utils.loads import json_path, load_json_data

router = APIRouter()


@router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token: str = create_token(
            user.model_dump()
        )  # Hay que tener cuidado con lo que se pone en el payload, esto lo puede ver cualquiera con un debugger: https://jwt.io/
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=401, content={"message": "Credenciales inválidas, intente de nuevo"})


@router.post('/movies', tags=['movies'], status_code=201)
def create_movie(movie: Movie):
    db = SessionLocal()
    new_movie = MovieBD(**movie.model_dump())
    db.add(new_movie)
    db.commit()

    return movie
