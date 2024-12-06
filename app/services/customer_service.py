from crud.customer_crud import create_customer_in_db, update_customer_in_db, delete_customer_from_db, get_customer_by_id, get_all_customers
from models.customer import CustomerCreate, CustomerUpdate
from fastapi import HTTPException, Depends
from core.database import get_db

# Service function to create a new customer
async def create_customer_service(customer_data: CustomerCreate, db = Depends(get_db)):
    return await create_customer_in_db(customer_data, db)

# Service function to update an existing customer
async def update_customer_service(customer_id: str, customer_data: CustomerUpdate, db = Depends(get_db)):
    return await update_customer_in_db(customer_id, customer_data, db)

# Service function to delete a customer
async def delete_customer_service(customer_id: str, db = Depends(get_db)):
    return await delete_customer_from_db(customer_id, db)

# Service function to get a customer by ID
async def get_customer_service(customer_id: str, db = Depends(get_db)):
    customer = await get_customer_by_id(customer_id, db)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

# Service function to get all customers
async def get_all_customers_service(db = Depends(get_db)):
    return await get_all_customers(db)
