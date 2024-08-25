from pydantic import BaseModel
from typing import Optional

# Breed 
class BreedBase(BaseModel):
    name: str
    breed_origin: str
    weight: float
    height: float
    ear_type: str
    energy_level: str
    life_expectancy: int
    drooling_tendency: str
    snoring_tendency: str
    barking_tendency: str
    digging_tendency: str
    attention_need: str
    breed_for: str
    coat_length: str
    coat_type: str
    coat_colors: str
    grooming_need: str

class BreedCreate(BreedBase):
    pass

class BreedUpdate(BaseModel):
    name: Optional[str]
    breed_origin: Optional[str]
    weight: Optional[float]
    height: Optional[float]
    ear_type: Optional[str]
    energy_level: Optional[str]
    life_expectancy: Optional[int]
    drooling_tendency: Optional[str]
    snoring_tendency: Optional[str]
    barking_tendency: Optional[str]
    digging_tendency: Optional[str]
    attention_need: Optional[str]
    breed_for: Optional[str]
    coat_length: Optional[str]
    coat_type: Optional[str]
    coat_colors: Optional[str]
    grooming_need: Optional[str]

class BreedResponse(BreedBase):
    id: int

    class Config:
        orm_mode = True

# Dog
class DogBase(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    coat_colors: str
    
class DogCreate(DogBase):
    breed_id: int
    
class DogUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    weight: Optional[float]
    height: Optional[float]
    coat_colors: Optional[str]
    breed_id: Optional[int]  # Optionally include breed_id if you want to allow updating the breed
    
class DogResponse(DogBase):
    id: int
    # breed: BreedResponse # Include breed details in the dog response
    
    class Config:
        orm_mode = True
