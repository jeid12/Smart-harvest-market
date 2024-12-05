from pydantic import BaseModel, EmailStr, Field
from typing import List, Literal, Optional
from bson import ObjectId

# Pydantic model for farmer registration (common fields)
class FarmerBase(BaseModel):
    full_name: str = Field(..., description="Full name of the farmer")
    username: str = Field(..., description="Username of the farmer", min_length=4, max_length=20)
    email: EmailStr = Field(..., description="Email of the farmer")
    crop_name: List[str]  # List of crops the farmer grows
    phone_number: str = Field(..., description="Phone number of the farmer")
    gender: Literal['male', 'female', 'other'] = Field(..., description="Gender of the farmer")
    location: str = Field(..., description="Location of the farmer")
    role: str = "Farmer"  # Default role is "Farmer"

# Pydantic model for farmer creation (with password)
class FarmerCreate(FarmerBase):
    password: str = Field(..., description="Password of the farmer", min_length=8)  # Password for registration (should be hashed before storage)

# Pydantic model for returning a Farmer object with MongoDB's ObjectId
class Farmer(FarmerBase):
    pass

    class Config:
        # Allow Pydantic to work with MongoDB's ObjectId
        json_encoders = {
            ObjectId: str
        }

# Pydantic model for updating farmer info (optional fields for updates)
class FarmerUpdate(FarmerBase):
    password: Optional[str] = None  # Password can be optionally updated
