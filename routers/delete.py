import json

from config.database import SessionLocal
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.movies import MovieBD
from services.movies import MovieService

router = APIRouter()


@router.delete('/movies/{id}', tags=['movies'])
def delete_movies(id: int):
    db = SessionLocal()
    return MovieService(db).delete_movie(id)
