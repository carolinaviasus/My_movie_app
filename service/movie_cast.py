from models.moviecast import MovieCast as MovieCastModel
from schemas.movie_cast import MovieCast


class MovieCastService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movie_cast(self):
        result = self.db.query(MovieCast).all()
        return result

    def get_movie_cast_by_actor_id(self,actor_id:int):
        result = self.db.query(MovieCastModel).filter(MovieCastModel.actor_id == actor_id).first()
        return result

    def get_movie_cast_by_id(self,movie_id:int):
        result = self.db.query(MovieCastModel).filter(MovieCastModel.movie_id == movie_id).first()
        return result

    def get_movie_cast_by_role(self,role:str):
        result = self.db.query(MovieCastModel).filter(MovieCastModel.role == role).all()
        return result

    def create_movie_cast(self,movie_cast: MovieCastModel):
        new_cast = MovieCastModel(
            actor_id = movie_cast.actor_id,
            movie_id = movie_cast.movie_id,
            role = movie_cast.role
        )
        self.db.add(new_cast)
        self.db.commit()
        return

    #actualizar 
    def update_movie_cast(self, role:str, data:MovieCast):
        movie_cast.actor_id = data.actor_id
        movie_cast.movie_id = data.movie_id
        movie_cast = self.db.query(MovieCastModel).filter(MovieCastModel.role == movie_cast.role).first()
        self.db.commit()
        return

    # eliminar
    def delete_movie_cast(self,movie_id:int, data:MovieCast):
        self.db.delete(data)
        self.db.commit