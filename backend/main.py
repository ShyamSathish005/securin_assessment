from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Recipe
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/api/recipes")
def read_recipes(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
  
    skip = (page - 1) * limit
    
    query = db.query(Recipe)
    total = query.count()
    recipes = query.offset(skip).limit(limit).all()
    
    return {
        "total": total,
        "page": page,
        "data": recipes 
    }