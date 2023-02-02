from models.movie_direction import MovieDirection as MovieDirectionModel
from schemas.movie_direction import Movie_direction

class MovieDirectionService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movie_direction(self):
        result = self.db.query(MovieDirectionModel).all()
        return result
#  movie_id:int 
#     dir_id:int
    def get_movie_direction_by_movie_id(self, movie_id:int):
        result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.movie_id == movie_id).first()
        return result

    def get_movie_direction_by_dir_id(self, dir_id:int):
        result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.dir_id == dir_id).first()
        return result

        # create
    def create_movie_direction(self, movie_direction:Movie_direction):
        new_movie_direction = MovieDirectionModel(
            movie_id=movie_direction.movie_id,
            dir_id=movie_direction.dir_id
        )
        self.db.add(new_movie_direction)
        self.db.commit()
        return 

    # update
    def update_movie_direction(self, movie_id:int, data:Movie_direction):
        movie_direction = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.movie_id == movie_id).first()
        movie_direction.dir_id = data.dir_id
        self.db.commit()
        return 

    # delete
    def delete_movie_direction(self, movie_id:int):
        self.db.query(MovieDirectionModel).filter(MovieDirectionModel.movie_id == movie_id).delete()
        self.db.commit()
        return