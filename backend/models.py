from sqlalchemy import Column, Integer, JSON, String
from database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(JSON)
    instructions = Column(JSON)
    prep_time = Column(Integer, default=0)