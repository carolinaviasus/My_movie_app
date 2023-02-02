from models.rating import Rating as RatingModel
from schemas.rating import Rating

class RatingService():

    def __init__(self,db) -> None:
        self.db = db

    def get_rating(self):
        result = self.db.query(RatingModel).all()
        return result

    # movie_id: int
    # rev_id: int
    # rev_starts: int
    # num_o_ratings: int

    def get_rating_movie_id(self,movie_id:int):
        result = self.db.query(RatingModel).filter(RatingModel.movie_id == movie_id).first()
        return result

    def get_rating_movie_rev_id(self,rev_id:int):
        result = self.db.query(RatingModel).filter(RatingModel.rev_id == rev_id).first()
        return result

    def get_rating_movie_rev_starts(self, rev_starts:int):
        result = self.db.query(RatingModel).filter(RatingModel.rev_starts == rev_starts).all()
        return result

    def get_rating_movie_num_o_ratings(self, num_o_ratings:int):
        result = self.db.query(RatingModel).filter(RatingModel.num_o_ratings == num_o_ratings).all()
        return result

        # create
    def create_rating(self, rating:Rating):
        new_rating = RatingModel(
            movie_id=rating.movie_id,
            rev_id=rating.rev_id,
            rev_starts=rating.rev_starts,
            num_o_ratings=rating.num_o_ratings
        )
        self.db.add(new_rating)
        self.db.commit()
        return 

        # update
    def update_rating(self, rev_starts:int, data:Rating):
        rating.movie_id = data.movie_id
        rating.rev_id = data.rev_id
        rating = self.db.query(RatingModel).filter(RatingModel.rev_stars == rev_starts).first()
        self.db.commit()
        return 

        # delete
    def delete_rating(self, rev_id:int):
        self.db.query(RatingModel).filter(RatingModel.rev_id == rev_id).delete()
        self.db.commit()
        return