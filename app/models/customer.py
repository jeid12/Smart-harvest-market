from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Optional
from bson import ObjectId

# Pydantic model for customer registration
class CustomerBase(BaseModel):
    full_name: str = Field(..., description="Full name of the customer")
    email: EmailStr = Field(..., description="Email of the customer")
    username: str = Field(..., description="Username of the customer", min_length=4, max_length=20)
    phone_number: str= Field(..., description="Phone number of the customer")
    address: str  = Field(..., description="Address of the customer")  # Customer's address for delivery or further contact
    role: str = "Customer"  # Default role is "Customer"
    gender:Literal['male', 'female', 'other'] = Field(..., description="Gender of the customer")

# Pydantic model for customer creation (with password)
class CustomerCreate(CustomerBase):
    password: str = Field(..., description="Password of the customer", min_length=8) # Password for registration (should be hashed before storage)

# Pydantic model for returning a Customer object with MongoDB's ObjectId
class Customer(CustomerBase):
    id

    class Config:
        allow_population_by_field_name = True
        # Allow Pydantic to work with MongoDB's ObjectId
        json_encoders = {
            ObjectId: str
        }

# Pydantic model for updating customer info (optional fields for updates)
class CustomerUpdate(CustomerBase):
    password: Optional[str] = None  # Password can be optionally updated
