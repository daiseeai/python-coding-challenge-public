from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


app = FastAPI()

class Price(Enum):
    LOW = "$10k"
    MEDIUM= "$20K"
    HIGH = "$30K"

class CarBase(BaseModel):
    car_name: str = Field(...,min_length=3, max_length=512, description="name of car" )
    car_brand: str = Field(...,min_length=3, max_length=512, description="brand of car" )
    car_description: str = Field(...,description="description")
    price: Price = Field(default=Price.LOW, description="price of car")

class Car(CarBase):
    car_id: int = Field(...,description="uniqueIdentifier of car")

class CarUpdate(BaseModel):
    car_name: Optional[str] = Field(...,min_length=3, max_length=512, description="name of car" )
    car_brand: Optional[str] = Field(...,min_length=3, max_length=512, description="brand of car" )
    car_description: Optional[str] = Field(...,description="description")
    price: Optional[Price] = Field(default=Price.LOW, description="price of car")


all_cars = [
    Car(car_id= 1, car_name = "63 GT", car_brand = "Mercedes-AMG", car_description = "expensive  german car", price = Price.HIGH),
        Car(car_id= 2, car_name = "488 SUPERFAST", car_brand = "Ferrari", car_description = "expensive italian car", price = Price.HIGH),
            Car(car_id= 3, car_name = "AVENTADOR", car_brand = "Lamborghini", car_description = "expensive italian car also", price = Price.HIGH),
                Car(car_id= 4, car_name = "SENNA", car_brand = "Mclaren", car_description= "expensive car", price = Price.HIGH),
] 



@app.get("/")
def root():
    return{"hello:world"}

@app.get("/cars/{car_id}", response_model= Car)

async def get_car(car_id: int):
    for car in all_cars:
        if car.car_id == car_id:
            return car
        
    raise HTTPException(status_code=404, detail="not found")

@app.get("/cars", response_model=List[Car])
async def get_all_cars():
   
     return all_cars
 

@app.post("/cars/{car_id}" ,response_model= Car)
async def create_car(car: CarBase):
     new_car_id = max(car.car_id for car in all_cars) + 1

     new_car = Car(
         car_id = new_car_id,
         car_name = car.car_name,
         car_brand = car.car_brand,
         car_description = car.car_description,
         price= car.price,
     )

     all_cars.append(new_car)
     return new_car 
     
@app.put('/cars/{car_id}', response_model= Car)
async def car_update(car_id: int , updated_car: CarUpdate):
   for car in all_cars:
    if car.car_id == car_id:
       if updated_car.car_name is not None:
           car.car_name = updated_car.car_name
       if updated_car.car_brand is not None:
           car.car_brand = updated_car.car_brand
       if updated_car.car_description is not None:
          car.car_description = updated_car.car_description
       if updated_car.price is not None:
          car.price = updated_car.price
       return car
    
   raise HTTPException(status_code=404, detail="not found")


@app.delete('/cars/{car_id}', response_model= Car)
async def delete_car(car_id: int):
   for index, car in enumerate(all_cars):
      if car.car_id == car_id:
         deleted_car =  all_cars.pop(index)
         return deleted_car
         
   raise HTTPException(status_code=404, detail="not found")
