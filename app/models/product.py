from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

# Pydantic model for creating a product (for farmer to post a product)
class ProductBase(BaseModel):
    name: str  = Field(..., description="Name of the product") # Name of the product
    description: str = Field(..., description="Description of the product")  # Description of the product
    price: float = Field(..., description="Price of the product")  # Price of the product
    quantity: int = Field(..., description="Quantity of the product")  # Available quantity of the product
    category: str = Field(..., description="Category of the product")  # Category of the product (e.g., fruits, vegetables, etc.)
    farmer_id: str = Field(..., description="ID of the farmer who posted the product")  # The ID of the farmer who posted the product
    warehouse_id: str = Field(..., description="ID of the warehouse where the product is stored")  # The ID of the warehouse where the product is stored
    image_url: Optional[str] = None  # Optional image URL for the product
    is_available: bool = True  # Whether the product is currently available for sale

#pydantic model for creating a new product
class  ProductCreate(ProductBase):
       pass #Inherits all fields from ProductBase (no extra fields for creation)

# Pydantic model for returning a Product object with MongoDB's ObjectId
class Product(ProductBase):
    id: str = Field(..., alias="_id", description="ID of the product")  # MongoDB stores the ObjectId as _id

    class Config:
        # Allow Pydantic to work with MongoDB's ObjectId
        json_encoders = {
            ObjectId: str
        }

# Pydantic model for updating product details (fields are optional)
class ProductUpdate(ProductBase):
    name: Optional[str] = None  # Name can be updated
    description: Optional[str] = None  # Description can be updated
    price: Optional[float] = None  # Price can be updated
    quantity: Optional[int] = None  # Quantity can be updated
    category: Optional[str] = None  # Category can be updated
    image_url: Optional[str] = None  # Image URL can be updated
    is_available: Optional[bool] = None  # Availability status can be updated
