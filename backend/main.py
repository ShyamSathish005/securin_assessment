from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc 
from database import get_db
from models import Recipe
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/api/recipes")
def read_recipes(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
   
    skip = (page - 1) * limit
    
 
    recipes = db.query(Recipe).order_by(desc(Recipe.rating)).offset(skip).limit(limit).all()
    total = db.query(Recipe).count()
    
    return {
        "total": total,
        "page": page,
        "data": recipes 
    }


@app.get("/api/recipes/search")
def search_recipes(q: str, page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * limit
    
    filtered = db.query(Recipe).filter(Recipe.title.ilike(f"%{q}%")).order_by(desc(Recipe.rating))
    recipes = filtered.offset(skip).limit(limit).all()
    total = filtered.count()
    
    return {
        "total": total,
        "page": page,
        "data": recipes 
    }