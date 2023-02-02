from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from config.database import Base
from models.actor import Director



class MovieDirection(Base):

    __tablename__ = "movie_direction"

    dir_id = Column(Integer, ForeignKey("director.id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
