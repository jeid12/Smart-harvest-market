from crud.warehouse_crud import (
    create_warehouse_in_db,
    get_all_warehouses,
    get_warehouse_by_id,
    update_warehouse_in_db,
    delete_warehouse_from_db
)
from models.warehouse import WarehouseCreate, WarehouseUpdate
from fastapi import Depends
from core.database import get_db

# Service function to create a new warehouse
async def create_warehouse_service(warehouse_data: WarehouseCreate, db=Depends(get_db)):
    return await create_warehouse_in_db(warehouse_data, db)

# Service function to get all warehouses
async def get_all_warehouses_service(db=Depends(get_db)):
    return await get_all_warehouses(db)

# Service function to get a warehouse by ID
async def get_warehouse_service(warehouse_id: str, db=Depends(get_db)):
    return await get_warehouse_by_id(warehouse_id, db)

# Service function to update a warehouse
async def update_warehouse_service(warehouse_id: str, warehouse_data: WarehouseUpdate, db=Depends(get_db)):
    return await update_warehouse_in_db(warehouse_id, warehouse_data, db)

# Service function to delete a warehouse
async def delete_warehouse_service(warehouse_id: str, db=Depends(get_db)):
    return await delete_warehouse_from_db(warehouse_id, db)
