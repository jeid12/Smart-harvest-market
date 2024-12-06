from fastapi import HTTPException
from bson import ObjectId
from models.farmer import FarmerCreate, Farmer, FarmerUpdate
from core.utils import str_to_object_id
from core.database import db
from typing import List


# Create a new farmer
async def create_farmer(db, farmer_data: FarmerCreate) -> Farmer:
    # Convert farmer data to dictionary and hash password (if necessary)
    farmer_dict = farmer_data.dict(exclude_unset=True)
    
    # Assuming password hashing (use a proper password hash function in practice)
    # farmer_dict['password'] = hash_password(farmer_data.password)
    
    # Insert farmer into the database
    result = await db.farmers.insert_one(farmer_dict)
    
    # Retrieve the inserted farmer
    created_farmer = await db.farmers.find_one({"_id": result.inserted_id})
    
    if created_farmer is None:
        raise HTTPException(status_code=400, detail="Farmer creation failed")
    
    # Return the created farmer with ObjectId converted to string
    return Farmer(**created_farmer, id=str(created_farmer["_id"]))

# Get all farmers
async def get_all_farmers(db) -> List[Farmer]:
    farmers_cursor = db.farmers.find()
    farmers = await farmers_cursor.to_list(length=100)  # You can adjust length as needed
    return [Farmer(**farmer, id=str(farmer["_id"])) for farmer in farmers]

# Get farmer by ID
async def get_farmer_by_id(db, farmer_id: str) -> Farmer:
    object_id = str_to_object_id(farmer_id)
    farmer = await db.farmers.find_one({"_id": object_id})
    
    if not farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    
    return Farmer(**farmer, id=str(farmer["_id"]))

# Update farmer's details
async def update_farmer(db, farmer_id: str, farmer_data: FarmerUpdate) -> Farmer:
    object_id = str_to_object_id(farmer_id)
    
    # Convert data to dictionary and update only fields that are provided
    update_data = {key: value for key, value in farmer_data.dict(exclude_unset=True).items()}
    
    # Update the farmer document
    result = await db.farmers.update_one({"_id": object_id}, {"$set": update_data})
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Farmer not found")
    
    # Retrieve the updated farmer document
    updated_farmer = await db.farmers.find_one({"_id": object_id})
    
    return Farmer(**updated_farmer, id=str(updated_farmer["_id"]))

# Delete a farmer by ID
async def delete_farmer(db, farmer_id: str) -> str:
    object_id = str_to_object_id(farmer_id)
    
    result = await db.farmers.delete_one({"_id": object_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Farmer not found")
    
    return "Farmer deleted successfully"



# Get farmer by username
async def get_farmer_by_name(username: str):
    farmer = await db["farmers"].find_one({"username": username})
    return farmer

# Get farmer by email
async def get_farmer_by_email(email: str):
    farmer = await db["farmers"].find_one({"email": email})
    return farmer
