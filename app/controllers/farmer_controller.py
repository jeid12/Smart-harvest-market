from fastapi import APIRouter, Depends
from models.farmer import FarmerCreate, Farmer, FarmerUpdate
from crud.farmer_crud import create_farmer, get_all_farmers, get_farmer_by_id, update_farmer, delete_farmer
from core.database import get_db  # You can adjust the database connection as needed
from typing import List

router = APIRouter()

# Route to create a new farmer
@router.post("/farmers/", response_model=Farmer)
async def create_farmer_route(farmer_data: FarmerCreate, db=Depends(get_db)):
    return await create_farmer(db, farmer_data)

# Route to get all farmers
@router.get("/farmers/", response_model=List[Farmer])
async def get_all_farmers_route(db=Depends(get_db)):
    return await get_all_farmers(db)

# Route to get farmer by ID
@router.get("/farmers/{farmer_id}", response_model=Farmer)
async def get_farmer_by_id_route(farmer_id: str, db=Depends(get_db)):
    return await get_farmer_by_id(db, farmer_id)

# Route to update farmer's information
@router.put("/farmers/{farmer_id}", response_model=Farmer)
async def update_farmer_route(farmer_id: str, farmer_data: FarmerUpdate, db=Depends(get_db)):
    return await update_farmer(db, farmer_id, farmer_data)

# Route to delete a farmer
@router.delete("/farmers/{farmer_id}")
async def delete_farmer_route(farmer_id: str, db=Depends(get_db)):
    return await delete_farmer(db, farmer_id)
