import json

from fastapi import APIRouter
from models.movies import Movie
from utils.loads import json_path, load_json_data

router = APIRouter()


@router.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    movies = load_json_data()

    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category

            with open(json_path, 'w') as file:
                json.dump(movies, file, indent=4)

            return movies
