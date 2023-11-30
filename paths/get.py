from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import HTMLResponse
from utils.loads import load_json_data

router = APIRouter()


@router.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')


@router.get('/movies', tags=['movies'])
def get_movies():
    return load_json_data()


@router.get('/movies/{id}', tags=['movies'])
def get_movie(id: int = Path(ge=1, le=2000)):
    movies = load_json_data()

    for item in movies:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Movie not found")


@router.get(
    '/movies/', tags=['movies']
)  # Se pone la barra al final de la url para indicar que vamos a recibir parámetros
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    movies = load_json_data()
    return [movie for movie in movies if movie['category'] == category]
