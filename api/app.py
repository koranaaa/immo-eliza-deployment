from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from predict import predict_price, validate_input  # Import function from predict.py
import pandas as pd

app = FastAPI()

class PropertyData(BaseModel):
    Number_of_bedrooms: int
    Living_area_m2: int
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
    print("Received data:", data_dict)  # Debug output

    # check the data using validate_input
    try:
        validate_input(data_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # get a forecast using predict_price
    try:
        prediction = predict_price(data_dict)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
