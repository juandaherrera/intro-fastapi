from typing import List

from sqlalchemy import func

from config.database import Base, SessionLocal, engine
from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from models.bearer import JWTBearer
from models.movies import Movie, MovieBD
from utils.loads import load_json_data

router = APIRouter()

Base.metadata.create_all(bind=engine)


@router.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')


@router.get('/movies', tags=['movies'], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies():
    db = SessionLocal()
    result = db.query(MovieBD).all()
    return JSONResponse(
        status_code=200, content=jsonable_encoder(result)
    )  # Este status code no es necesario porque ya se añadió en el decorador


@router.get('/movies/{id}', tags=['movies'], status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)):
    db = SessionLocal()
    result = db.query(MovieBD).filter(MovieBD.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': f'No se encontró ninguna película con el id {id}'})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@router.get(
    '/movies/', tags=['movies'], status_code=200
)  # Se pone la barra al final de la url para indicar que vamos a recibir parámetros
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    db = SessionLocal()
    result = db.query(MovieBD).filter(func.lower(MovieBD.category) == category.lower()).all()
    return jsonable_encoder(result)
