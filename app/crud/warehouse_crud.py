from models.warehouse import WarehouseCreate, WarehouseUpdate, Warehouse
from bson import ObjectId
from core.database import db
from fastapi import HTTPException, Depends
from pymongo.collection import Collection

# Get the database collection for warehouses


# Create a warehouse
async def create_warehouse_in_db(warehouse_data: WarehouseCreate, db: Collection ):
    # Insert the warehouse data into the MongoDB collection
    result = await db.wherehouses.insert_one(warehouse_data.dict())
    
    # Retrieve the created warehouse to include the MongoDB _id
    created_warehouse = await db.wherehouses.find_one({"_id": result.inserted_id})
    
    return Warehouse(**created_warehouse)

# Get all warehouses
async def get_all_warehouses(db: Collection ):
    warehouses_cursor = db.wherehouses.find({})
    warehouses = [Warehouse(**warehouse) async for warehouse in warehouses_cursor]
    return warehouses

# Get a warehouse by ID
async def get_warehouse_by_id(warehouse_id: str, db: Collection ):
    warehouse = await db.wherehouses.find_one({"_id": ObjectId(warehouse_id)})
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return Warehouse(**warehouse)

# Update a warehouse
async def update_warehouse_in_db(warehouse_id: str, warehouse_data: WarehouseUpdate, db: Collection ):
    # Ensure the warehouse exists before updating
    existing_warehouse = await get_warehouse_by_id(warehouse_id, db)
    if not existing_warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    
    # Update the warehouse in the database
    update_data = {key: value for key, value in warehouse_data.dict(exclude_unset=True).items()}
    await db.wherehouses.update_one({"_id": ObjectId(warehouse_id)}, {"$set": update_data})
    
    # Retrieve the updated warehouse
    updated_warehouse = await db.wherehouses.find_one({"_id": ObjectId(warehouse_id)})
    return Warehouse(**updated_warehouse)

# Delete a warehouse
async def delete_warehouse_from_db(warehouse_id: str, db: Collection ):
    # Ensure the warehouse exists before deleting
    existing_warehouse = await get_warehouse_by_id(warehouse_id, db)
    if not existing_warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    
    # Delete the warehouse
    await db.wherehouses.delete_one({"_id": ObjectId(warehouse_id)})
    return {"message": "Warehouse deleted successfully"}
