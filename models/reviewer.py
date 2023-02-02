from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Reviewer(Base):
    __tablename__ = "reviewer"

    id = Column(Integer, primary_key = True)
    name = Column(String)