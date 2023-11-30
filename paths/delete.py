import json

from fastapi import APIRouter
from utils.loads import json_path, load_json_data

router = APIRouter()


@router.delete('/movies/{id}', tags=['movies'])
def delete_movies(id: int):
    movies = load_json_data()

    for item in movies:
        if item['id'] == id:
            movies.remove(item)

            with open(json_path, 'w') as file:
                json.dump(movies, file, indent=4)
            return movies
