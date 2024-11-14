from fastapi import FastAPI, HTTPException
print("FastAPI imported successfully")
from pydantic import BaseModel, Field

from predict import predict_price, validate_input # Import function from predict.py
print("predict module imported successfully")

import pandas as pd

app = FastAPI()

class PropertyData(BaseModel):
    Number_of_bedrooms: int = Field(..., alias='Number of bedrooms')
    Living_area_m2: int = Field(..., alias="Living area m²")
    Equipped_kitchen: int
    Furnished: int
    Swimming_pool: int
    Building_condition: str
    Region: str
    Property_type: str

@app.get("/")
async def root():
    return {"status": "alive"}

@app.post("/predict")
async def get_prediction(data: PropertyData):
    # Сonvert the data into a dictionary for further use
    data_dict = data.dict()
    
    data_dict= {key.replace('_', ' '):value for key,value in data_dict.items()}

    print("Received data:", data_dict)  # Debug output


    # check the data using validate_input
    #try:
    #    print("Validating input data...")
    #    validate_input(data_dict)
    #    print("Validation successful.")
    #except ValueError as e:
    #    print(f"Validation error: {e}")
    #    raise HTTPException(status_code=400, detail=str(e))
    
    prediction = predict_price(data_dict)
    return {"prediction": prediction}

    # get a forecast using predict_price
    #try:
    #    print("Making prediction...")
    #    prediction = predict_price(data_dict)
    #    print("Prediction successful.")
    #    return {"prediction": prediction}
    #except Exception as e:
    #    print(f"Prediction error: {e}")
    #    raise HTTPException(status_code=500, detail=str(e))
