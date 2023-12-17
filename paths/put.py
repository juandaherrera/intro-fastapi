import json

from config.database import SessionLocal
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.movies import Movie, MovieBD
from utils.loads import json_path, load_json_data

router = APIRouter()


@router.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    db = SessionLocal()
    result = db.query(MovieBD).filter(MovieBD.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': f'No se encontró ninguna película con el id {id}'})

    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category

    db.add(result)
    db.commit()
    db.refresh(result)

    movie_response = {
        'message': f'La película con id {id} se ha actualizado con éxito',
    }
    return movie_response
