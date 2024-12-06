from fastapi import APIRouter, HTTPException, Depends
from models.customer import CustomerCreate, CustomerUpdate, Customer
from services.customer_service import create_customer_service, update_customer_service, delete_customer_service, get_customer_service, get_all_customers_service
from core.database import get_db

router = APIRouter()

@router.post("/customers", response_model=Customer)
async def create_customer_route(customer_data: CustomerCreate, db = Depends(get_db)):
    """
    Endpoint to register a new customer.
    """
    return await create_customer_service(customer_data, db)

@router.put("/customers/{customer_id}", response_model=Customer)
async def update_customer_route(customer_id: str, customer_data: CustomerUpdate, db = Depends(get_db)):
    """
    Endpoint to update an existing customer.
    """
    return await update_customer_service(customer_id, customer_data, db)

@router.delete("/customers/{customer_id}")
async def delete_customer_route(customer_id: str, db = Depends(get_db)):
    """
    Endpoint to delete a customer.
    """
    return await delete_customer_service(customer_id, db)

@router.get("/customers/{customer_id}", response_model=Customer)
async def get_customer_route(customer_id: str, db = Depends(get_db)):
    """
    Endpoint to get customer details by ID.
    """
    return await get_customer_service(customer_id, db)

@router.get("/customers", response_model=list[Customer])
async def get_all_customers_route(db = Depends(get_db)):
    """
    Endpoint to get all customers.
    """
    return await get_all_customers_service(db)
