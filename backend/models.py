from sqlalchemy import Column, String, Integer, Float, JSON, Text
from database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    

    cuisine = Column(String)
    title = Column(String)
    serves = Column(String) 
    

    rating = Column(Float)
    prep_time = Column(Integer)
    cook_time = Column(Integer)
    total_time = Column(Integer)
    
   
    description = Column(Text)
    
   
    nutrients = Column(JSON)