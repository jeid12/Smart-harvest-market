from crud.farmer_crud import (
    create_farmer_in_db, 
    get_all_farmers_from_db, 
    get_farmer_by_id_from_db, 
    update_farmer_in_db, 
    delete_farmer_from_db
)
from models.farmer import FarmerCreate, FarmerUpdate

# Service function to create a new farmer
async def create_farmer(farmer_data: FarmerCreate):
    return await create_farmer_in_db(farmer_data)

# Service function to get all farmers
async def get_all_farmers():
    return await get_all_farmers_from_db()

# Service function to get a farmer by ID
async def get_farmer_by_id(farmer_id: str):
    return await get_farmer_by_id_from_db(farmer_id)

# Service function to update a farmer's details
async def update_farmer(farmer_id: str, farmer_data: FarmerUpdate):
    update_data = farmer_data.dict(exclude_unset=True)  # Ignore unset fields (fields not provided)
    return await update_farmer_in_db(farmer_id, update_data)

# Service function to delete a farmer by ID
async def delete_farmer(farmer_id: str):
    return await delete_farmer_from_db(farmer_id)
