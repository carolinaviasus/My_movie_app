from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel, Field
from typing import Optional

class Reviewer(BaseModel):
    id: Optional[int] = None
    name: str =Field(max_length='20', min_length='3')

    class Config:
        schema_extra = {
            "example" : {
                'id':2,
                'name': 'Jhon',
            }
        }