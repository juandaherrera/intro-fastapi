from config.database import SessionLocal
from fastapi import APIRouter
from schemas.movies import Movie
from services.movies import MovieService

router = APIRouter()


@router.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    db = SessionLocal()
    return MovieService(db).update_movie(id, movie)
