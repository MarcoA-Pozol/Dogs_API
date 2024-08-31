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
    name: Optional[str] = None
    breed_origin: Optional[str] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    ear_type: Optional[str] = None
    energy_level: Optional[str] = None
    life_expectancy: Optional[int] = None
    drooling_tendency: Optional[str] = None
    snoring_tendency: Optional[str] = None
    barking_tendency: Optional[str] = None
    digging_tendency: Optional[str] = None
    attention_need: Optional[str] = None
    breed_for: Optional[str] = None
    coat_length: Optional[str] = None
    coat_type: Optional[str] = None
    coat_colors: Optional[str] = None
    grooming_need: Optional[str] = None

class BreedResponse(BreedBase):
    id: int

    class ConfigDict:
        from_attributes = True

# Dog
class DogBase(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    coat_colors: str
    breed_id: int
    
class DogCreate(DogBase):
    breed_id: int
    
class DogUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    coat_colors: Optional[str] = None
    breed_id: Optional[int] = None # Optionally include breed_id if you want to allow updating the breed
    
class DogResponse(DogBase):
    id: int
    # breed: BreedResponse # Include breed details in the dog response
    
    class ConfigDict:
        from_attributes = True
