from config.database import SessionLocal
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.movies import Movie
from schemas.users import User
from services.movies import MovieService
from utils.jwt_manager import create_token

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
    new_movie = MovieService(db).create_movie(movie)

    return new_movie
