from fastapi import APIRouter, Depends
from models.warehouse import WarehouseCreate, WarehouseUpdate, Warehouse
from services.warehouse_service import (
    create_warehouse_service,
    get_all_warehouses_service,
    get_warehouse_service,
    update_warehouse_service,
    delete_warehouse_service
)
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=Warehouse)
async def create_warehouse_route(warehouse_data: WarehouseCreate, db=Depends(get_db)):
    """
    Create a new warehouse.
    """
    return await create_warehouse_service(warehouse_data, db)

@router.get("/", response_model=list[Warehouse])
async def get_all_warehouses_route(db=Depends(get_db)):
    """
    Retrieve all warehouses.
    """
    return await get_all_warehouses_service(db)

@router.get("/{warehouse_id}", response_model=Warehouse)
async def get_warehouse_route(warehouse_id: str, db=Depends(get_db)):
    """
    Retrieve a warehouse by its ID.
    """
    return await get_warehouse_service(warehouse_id, db)

@router.put("/{warehouse_id}", response_model=Warehouse)
async def update_warehouse_route(warehouse_id: str, warehouse_data: WarehouseUpdate, db=Depends(get_db)):
    """
    Update an existing warehouse.
    """
    return await update_warehouse_service(warehouse_id, warehouse_data, db)

@router.delete("/{warehouse_id}")
async def delete_warehouse_route(warehouse_id: str, db=Depends(get_db)):
    """
    Delete a warehouse.
    """
    return await delete_warehouse_service(warehouse_id, db)
