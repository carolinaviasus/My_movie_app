from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from config.database import Session

from models.movie_direction import MovieDirection as MovieDirectionModel
from service.movie_direction import MovieDirectionService
from schemas.movie_direction import Movie_direction

Movie_direction_router = APIRouter()


@Movie_direction_router.get("/movie_direction", response_model=List[Movie_direction],status_code=200)
def get_movie_direction() -> Movie_direction:
    db = Session()
    result = MovieDirectionService(db).get_movie_direction()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@Movie_direction_router.get('/movie_direction/{movie_id}',tags=['movie_direction'])
def get_movie_direction_by_id(movie_id: int = Path(ge=1, le=200)):
    db = Session()
    result = MovieDirectionService(db).get_movie_direction_by_id(movie_id)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)



