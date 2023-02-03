from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from config.database import Session

from models.rating import Rating as RatingModel
from service.rating import RatingService
from schemas.rating import Rating

rating_router = APIRouter()

@rating_router.get("/rating", tags=['rating'], response_model=List[Rating], status_code=200)
def get_rating() -> Rating:
    db = Session()
    result = RatingService(db).get_rating(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@rating_router.post("/rating", tags=['rating'], response_model=dict,status_code=201)
def create_rating(rating: RatingModel) -> dict:
    db = Session()
    RatingService.create_rating(db,rating)
    return JSONResponse(content={"message": "has been created successfully", "status_code":"201"})

@rating_router.put("/rating/{id}", tags=['rating'])
def update_rating(id: int, rating: RatingModel):
    db = Session
    result = RatingService(db).get_rating(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found"})
    RatingService(db).update_rating(id,rating)
    return JSONResponse(content={"message": "has been modific successfully", "status_code":"201"})

@rating_router.delete("/rating/{id}", tags=['rating'], response_model=dict, status=200)
def delete_rating(id:int ) -> dict:
    db = Session()
    result = RatingModel = db.query(RatingModel).filter(RatingModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found"})
    RatingService(db).delete_rating(id)
    return JSONResponse(content={"message": "has been deleted successfully", "status_code":"200"})
