from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId

# Pydantic model for transaction details
class TransactionBase(BaseModel):
    customer_id: str  # The ID of the customer making the purchase
    farmer_id: str  # The ID of the farmer selling the product
    product_id: str  # The ID of the product being purchased
    quantity: int  # The quantity of the product purchased
    total_price: float  # Total price of the transaction (calculated as price * quantity)
    status: str  # Status of the transaction (e.g., 'pending', 'completed', 'cancelled')
    date: str  # Date of the transaction (can be in ISO format or custom format)

# Pydantic model for creating a new transaction
class TransactionCreate(TransactionBase):
    pass  # Inherits all fields from TransactionBase (no extra fields for creation)

# Pydantic model for returning a transaction object with MongoDB's ObjectId
class Transaction(TransactionBase):
    id: str = Field(..., alias="_id")  # MongoDB stores the ObjectId as _id

    class Config:
        # Allow Pydantic to work with MongoDB's ObjectId
        json_encoders = {
            ObjectId: str
        }

# Pydantic model for updating a transaction status (optional fields)
class TransactionUpdate(BaseModel):
    status: str  # Status can be updated (e.g., from 'pending' to 'completed')
    # Add other fields if you want to update any other data
