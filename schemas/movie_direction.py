from pydantic import BaseModel

class Movie_direction(BaseModel):
    movie_id:int 
    dir_id:int

    class Config:
        schema_extra = {
            "example":{
                "movie_id": 3,
                "dir_id": 3,
            }
        }