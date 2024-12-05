from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

# Pydantic model for warehouse details
class WarehouseBase(BaseModel):
    name: str  # Name of the warehouse
    location: str  # Location of the warehouse (e.g., city, district)
    capacity: int  # Total capacity of the warehouse in terms of space or volume
    available_space: int  # Available space in the warehouse for new products
    product_ids: list = []  # List of product IDs stored in the warehouse
    description: Optional[str] = None  # Optional description about the warehouse

# Pydantic model for creating a new warehouse
class WarehouseCreate(WarehouseBase):
    pass  # Inherits all fields from WarehouseBase (no extra fields for creation)

# Pydantic model for returning a warehouse object with MongoDB's ObjectId
class Warehouse(WarehouseBase):
    id: str = Field(..., alias="_id")  # MongoDB stores the ObjectId as _id

    class Config:
        # Allow Pydantic to work with MongoDB's ObjectId
        json_encoders = {
            ObjectId: str
        }

# Pydantic model for updating a warehouse (optional fields for update)
class WarehouseUpdate(BaseModel):
    name: Optional[str] = None  # Warehouse name can be updated
    location: Optional[str] = None  # Location can be updated
    capacity: Optional[int] = None  # Capacity can be updated
    available_space: Optional[int] = None  # Available space can be updated
    description: Optional[str] = None  # Optional description can be updated
