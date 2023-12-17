from sqlalchemy import func
from sqlalchemy.orm.session import Session

from fastapi.responses import JSONResponse
from models.movies import MovieBD
from schemas.movies import Movie


class MovieService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieBD).all()
        return result

    def get_movie(self, id: int):
        result = self.db.query(MovieBD).filter(MovieBD.id == id).first()
        return result

    def get_movie_by_category(self, category: str):
        result = self.db.query(MovieBD).filter(func.lower(MovieBD.category) == category.lower()).all()
        return result

    def create_movie(self, movie: Movie):
        new_movie = MovieBD(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return movie

    def update_movie(self, id: int, data: Movie):
        movie = self.get_movie(id)

        if not movie:
            return JSONResponse(status_code=404, content={'message': f'No se encontró ninguna película con el id {id}'})

        # Actualizar los campos de la película
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(movie, key, value)

        self.db.commit()
        self.db.refresh(movie)

        return {'message': f'La película con id {id} se ha actualizado con éxito'}

    def delete_movie(self, id: int):
        movie = self.get_movie(id)

        if not movie:
            return JSONResponse(status_code=404, content={'message': f'No se encontró ninguna película con el id {id}'})

        self.db.delete(movie)
        self.db.commit()

        return JSONResponse(status_code=200, content={'message': f'Se ha eliminado correctamente la película {id}'})
