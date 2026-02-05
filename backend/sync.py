import json
import os
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

def sync_recipes():
    db = SessionLocal()
    

    desktop_path = os.path.expanduser("/Users/shyamsathish/Desktop/US_recipes_null.json")
    
    with open(desktop_path, 'r') as file:
        recipes_data = json.load(file)

        for r in recipes_data.values():

            new_recipe = models.Recipe(
                name=r.get('title'),
                ingredients=r.get('ingredients'),
                instructions=r.get('instructions'),
                prep_time=r.get('prep_time', 0)
            )
            
            db.add(new_recipe)
            
    db.commit()
    db.close()
    print("Recipes synced successfully!")

if __name__ == "__main__":
    sync_recipes()