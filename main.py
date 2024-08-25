from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, db
# Import the DB configurations to be used
from db import get_db, SessionLocal


"""API CONFIG"""
app = FastAPI()

# Create the tables
models.Base.metadata.create_all(bind=db.engine)


"""ENDPOINTS"""
# [GET]
@app.get("/dogs/{dog_id}", response_model=schemas.DogResponse)
def get_dog(dog_id: int, db: Session = Depends(get_db)):
    db_dog = db.query(models.Dog).filter(models.Dog.id == dog_id).first()
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return db_dog

@app.get("/dogs/", response_model=list[schemas.DogResponse])
def get_dogs_list(db: Session = Depends(get_db)):
    dogs = db.query(models.Dog).all()
    return dogs

@app.get("/breeds/{breed_id}", response_model=schemas.BreedResponse)
def get_breed(breed_id: int, db: Session = Depends(get_db)):
    db_breed = db.query(models.Breed).filter(models.Breed.id == breed_id).first()
    if db_breed is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    return db_breed

@app.get("/breeds/", response_model=list[schemas.BreedResponse])
def get_breeds_list(db: Session = Depends(get_db)):
    breeds = db.query(models.Breed).all()
    return breeds

    
# [POST]
@app.post("/breeds/", response_model=schemas.BreedResponse)
def create_breed(breed: schemas.BreedCreate, db: Session = Depends(get_db)):
    db_breed = models.Breed(**breed.model_dump())
    db.add(db_breed)
    db.commit()
    db.refresh(db_breed)
    return db_breed

@app.post("/dogs/", response_model=schemas.DogResponse)
def create_dog(dog: schemas.DogCreate, db: Session = Depends(get_db)):
    db_breed = db.query(models.Breed).filter(models.Breed.id == dog.breed_id).first()
    if db_breed is None:
        raise HTTPException(status_code=400, detail="Breed not found")
    db_dog = models.Dog(**dog.model_dump())
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog
    
# [PUT]
@app.put("/breeds/{breed_id}", response_model=schemas.BreedResponse)
def update_breed(breed_id: int, breed: schemas.BreedUpdate, db: Session = Depends(get_db)):
    db_breed = db.query(models.Breed).filter(models.Breed.id == breed_id).first()
    if db_breed is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    for key, value in breed.model_dump().items():
        setattr(db_breed, key, value)
    db.commit()
    db.refresh(db_breed)
    return db_breed

@app.put("/dogs/{dog_id}", response_model=schemas.DogResponse)
def update_dog(dog_id: int, dog: schemas.DogUpdate, db: Session = Depends(get_db)):
    db_dog = db.query(models.Dog).filter(models.Dog.id == dog_id).first()
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    for key, value in dog.model_dump().items():
        setattr(db_dog, key, value)
    db.commit()
    db.refresh(db_dog)
    return db_dog

# [PATCH]
@app.patch("/breeds/{breed_id}", response_model=schemas.BreedResponse)
def update_breed(breed_id: int, breed_update: schemas.BreedUpdate, db: Session = Depends(get_db)):
    db_breed = db.query(models.Breed).filter(models.Breed.id == breed_id).first()
    if db_breed is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    
    # Update breed attributes
    for key, value in breed_update.dict(exclude_unset=True).items():
        setattr(db_breed, key, value)
    
    db.commit()
    db.refresh(db_breed)
    return db_breed

@app.patch("/dogs/{dog_id}", response_model=schemas.DogResponse)
def update_dog(dog_id: int, dog_update: schemas.DogUpdate, db: Session = Depends(get_db)):
    db_dog = db.query(models.Dog).filter(models.Dog.id == dog_id).first()
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    
    # Update dog attributes
    for key, value in dog_update.dict(exclude_unset=True).items():
        setattr(db_dog, key, value)
    
    # If breed_id is updated, ensure the new breed exists
    if dog_update.breed_id is not None:
        db_breed = db.query(models.Breed).filter(models.Breed.id == dog_update.breed_id).first()
        if db_breed is None:
            raise HTTPException(status_code=400, detail="Breed not found")
    
    db.commit()
    db.refresh(db_dog)
    return db_dog

    
# [DELETE]
@app.delete("/breeds/{breed_id}", response_model=schemas.BreedResponse)
def delete_breed(breed_id: int, db: Session = Depends(get_db)):
    """Deletes a breed from the DB using DELETE method with an API endpoint."""
    
    breed = db.query(models.Breed).filter(models.Breed.id == breed_id).first()
    if breed is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    db.delete(breed)
    db.commit()
    return breed

@app.delete("/dogs/{dog_id}", response_model=schemas.DogResponse)
def delete_dog(dog_id: int, db: Session = Depends(get_db)):
    """Deletes a dog from the DB using DELETE method with an API endpoint."""
    
    dog = db.query(models.Dog).filter(models.Dog.id == dog_id).first()
    if dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    db.delete(dog)
    db.commit()
    return dog