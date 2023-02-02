from pydantic import BaseModel

class Rating(BaseModel):

    movie_id: int
    rev_id: int
    rev_starts: int
    num_o_ratings: int

    class Config:
        schema_extra = {
            "example":{
                'movie_id': 3,
                'rev_id': 3,
                'rev_starts': 4,
                'num_o_ratings': 10,
            }
        } 