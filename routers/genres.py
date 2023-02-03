from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from config.database import Session

from models.genres import Genres as GenresModel
from service.genres import GenresService
from schemas.genres import Genres

genres_router = APIRouter()

@genres_router.get("/genres", tags=['genres'], response_model=List[Genres],status_code=200)
def get_genres() -> Genres:
    db:Session()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@genres_router.get("/genres/{id}", tags=['genres'])
def get_genres_by_id(id:int = Path(ge=1, le=2000)):
    db:Session()
    result = GenresService(db).get_genres_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found"})
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@genres_router.post("/genres", tags=['genres'], response_model=dict, status_code=201)
def create_genres(genres: Genres)-> dict:
    db:Session()
    GenresService.create_genres(db,genres)
    return JSONResponse(content={"message":"has been registered", "status_code":"201"})

@genres_router.put("/genres/{id}", tags=['genres'])
def update_genres(id:int, genres: Genres):
    db = Session
    result = GenresService(db).get_genres(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found"})
    GenresService(db).update_genres(id, genres)
    return JSONResponse(content={"message": "genres updated with id: {id}"})

@genres_router.delete("/genres/{id}", tags=['genres'], response_model=dict, status_code=200)
def delete_genres(id:int)-> dict:
    db:Session()
    result: GenresModel =db.query(GenresModel).filter(GenresModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found"})
    GenresService(db).delete_genres(id)
    return JSONResponse(status_code=200, content={"message": "has been deleted"})