from pydantic import BaseModel, Field
from typing import Annotated
from enum import Enum

class FuelType(str, Enum):
    petrol = "Petrol"
    diesel = "Diesel"
    cng = "CNG"
    
class SellerType(str, Enum):
    dealer = "Dealer"
    individual = "Individual"
    
class TransmissionType(str, Enum):
    automatic = "Automatic"
    manual = "Manual"

class CarFeatures(BaseModel):
    Car_Name: Annotated[str, Field(example='ritz')]
    Year: Annotated[str, Field(example='2017')]
    Present_Price: Annotated[float, Field(strict=True, description="In lacs", example=5.9)]
    Kms_Driven: Annotated[int, Field(example=27000)]
    Owner: Annotated[int, Field(ge=0, le=3, description="Number of past owners")]
    Fuel_Type: FuelType
    Seller_Type: SellerType
    Transmission: TransmissionType
    
class PredictionResponse(BaseModel):
    prediction_price: Annotated[float, Field(strict=True, ge=0, description="Predicted price of the car")]