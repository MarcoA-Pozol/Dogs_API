from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Breed(Base):
    __tablename__ = "breeds"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    breed_origin = Column(String, index=True) # Country
    # Weight
    weight = Column(Float) # In Kg
    # Height
    height = Column(Float) # In centimeters
    # Characteristics
    ear_type = Column(String)  # E.g., "upright"
    # Expectations
    energy_level = Column(String)  # E.g., "very energetic"
    life_expectancy = Column(Integer) # In years
    # Tendencies
    drooling_tendency = Column(String)  # E.g., "low"
    snoring_tendency = Column(String)  # E.g., "moderate to high"
    barking_tendency = Column(String)  # E.g., "moderate to high"
    digging_tendency = Column(String)  # E.g., "low"
    attention_need = Column(String)  # E.g., "high"
    # Purpose
    breed_for = Column(String)  # E.g., "companionship"
    # Coat
    coat_length = Column(String)  # E.g., "short/long"
    coat_type = Column(String)  # E.g., "flattened, smooth"
    coat_colors = Column(String)  # E.g., "any color"
    # Grooming
    grooming_need = Column(String)  # E.g., "low"
    # Relationship with Dog model
    dogs = relationship("Dog", back_populates="breed")
    
class Dog(Base):
    __tablename__ = "dogs"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    coat_colors = Column(String)
    
    # FK to connect Dog to Breed
    breed_id = Column(Integer, ForeignKey("breeds.id"))
    
    # Relationship with Breed model
    breed = relationship("Breed", back_populates="dogs")
    

# First breed to be posted using [POST] in the correct API endpoint to create and save the first Breed instance. 
"""{
  "name": "Chihuahua",
  "breed_origin": "Mexico",
  "weight": 2.0,
  "height": 20.0,
  "ear_type": "Upright",
  "energy_level": "Very energetic",
  "life_expectancy": 16,
  "drooling_tendency": "Low",
  "snoring_tendency": "Moderate to high",
  "barking_tendency": "Moderate to high",
  "digging_tendency": "Low",
  "attention_need": "High",
  "breed_for": "Companionship",
  "coat_length": "Shor, long",
  "coat_type": "Flattened, smooth",
  "coat_colors": "Any color",
  "grooming_need": "Low"
}"""