import json
import os
from database import SessionLocal, engine
import models

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

def sync_recipes():
    db = SessionLocal()
    

    path = os.path.expanduser("/Users/shyamsathish/Desktop/US_recipes_null.json")
    
    with open(path, 'r') as file:
        data = json.load(file)

        if isinstance(data, dict):
            items = data.values()
        elif isinstance(data, list):
            items = data
        else:
            items = []

        for item in items:
            if not isinstance(item, dict):
                continue

            new_recipe = models.Recipe(
                cuisine=item.get('cuisine'),
                title=item.get('title'),
                rating=item.get('rating'),
                prep_time=item.get('prep_time'),
                cook_time=item.get('cook_time'),
                total_time=item.get('total_time'),
                description=item.get('description'),
                nutrients=item.get('nutrients'),
                serves=item.get('serves')
            )
        
            db.add(new_recipe)
            

    db.commit()
    db.close()


if __name__ == "__main__":
    sync_recipes()