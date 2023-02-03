from fastapi import APIRouter, Path, Query
from models.director import Director as DirectorModel
from schemas.director import Director
from typing import List
from config.database import Session
from service.director import DirectorService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


director_router = APIRouter()



@director_router.get('/director', tags=['director'], response_model=List[Director], status_code=200)
def get_director() -> Director:
    db = Session()
    result = DirectorService(db).get_director()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

# hace validacion de datos o parametro path le >= ge<=
@director_router.get('/director/{id}', tags=['director'], response_model=Director, status_code=200)
def get_director_by_id(id: int = Path(ge=1, le=2000)):
    db = Session()
    result = DirectorService(db).get_director_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found director with that id"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.get('/director/', tags=['director'],response_model= List[Director], status_code=200)
def get_director_by_fname(fname:str = Query(min_length=2, max_length=20)):
    db = Session()
    result = db.query(DirectorModel).filter(DirectorModel.fname == fname).all()
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found :( "})
    return JSONResponse(content=jsonable_encoder(result), status_code=20)

@director_router.post('/director/', tags=['director'],status_code=200, response_model=dict)
def create_director(director: Director) -> dict:
    db = Session()
    DirectorService(db).create_director(director)
    return JSONResponse(content={"message":"Director create sucessfully","status_code":"201"})

@director_router.put('/director/{id}', tags=['director'])
def update_director(id: int, director: Director):
    db = Session()
    result = DirectorService(db).get_director(id)
    if not result:
        return JSONResponse(content={"message": "not found director with that id","status_code":"404"})
    DirectorService(db).update_director(id, director)
    return JSONResponse(content={"message": "The director with id: {id} has been modified" })

@director_router.delete('/director/{id}', tags=['director'],response_model=dict, status_code=200)
def delete_director(id: int) -> dict:
    db = Session()
    result = DirectorModel = db.query(DirectorModel).filter(DirectorModel.id == id).first()
    if not result:
        return JSONResponse(    content={"message": "not found director with that id","status_code":"404"})
    DirectorService(db).delete_director(id)
    return JSONResponse( content={"message": "has been removed"})