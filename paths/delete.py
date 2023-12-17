import json

from config.database import SessionLocal
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.movies import MovieBD
from utils.loads import json_path, load_json_data

router = APIRouter()


@router.delete('/movies/{id}', tags=['movies'])
def delete_movies(id: int):
    db = SessionLocal()
    result = db.query(MovieBD).filter(MovieBD.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': f'No se encontró ninguna película con el id {id}'})

    db.delete(result)
    db.commit()

    return JSONResponse(status_code=200, content={'message': f'Se ha eliminado correctamente la película {id}'})
