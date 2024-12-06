from models.customer import CustomerCreate, Customer, CustomerUpdate
from fastapi import HTTPException
from bson import ObjectId
from core.database import db
from pymongo.collection import Collection
from passlib.context import CryptContext

# Initialize CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



# Create a customer
async def create_customer_in_db(customer_data: CustomerCreate, db: Collection):
    

    # Check if a customer with the same email already exists
    existing_customer_by_email = await db.customers.find_one({"email": customer_data.email})
    if existing_customer_by_email:
        raise HTTPException(status_code=400, detail="Email already in use")

    # Check if a customer with the same username already exists
    existing_customer_by_username = await db.customers.find_one({"username": customer_data.username})
    if existing_customer_by_username:
        raise HTTPException(status_code=400, detail="Username already in use")

    # Hash the password before saving it
    hashed_password = pwd_context.hash(customer_data.password)
    customer_data.password = hashed_password

    # Insert the customer data into the MongoDB collection
    result = await db.customers.insert_one(customer_data.dict())

    # Retrieve the customer after insertion to get the MongoDB _id
    created_customer = await db.customers.find_one({"_id": result.inserted_id})

    return Customer(**created_customer)

# Get a customer by ID
async def get_customer_by_id(customer_id: str, db: Collection):
    
    customer = await db.customers.find_one({"_id": ObjectId(customer_id)})
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return Customer(**customer)

# Get a customer by email
async def get_customer_by_email(email: str):
    
    customer = await db.customers.find_one({"email": email})
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return Customer(**customer)

# Update a customer
async def update_customer_in_db(customer_id: str, customer_data: CustomerUpdate, db: Collection):
  

    # Fetch the existing customer to update
    existing_customer = await get_customer_by_id(customer_id)
    if not existing_customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # If password is updated, hash it before saving
    if customer_data.password:
        customer_data.password = pwd_context.hash(customer_data.password)

    # Update the customer in the database
    update_data = {key: value for key, value in customer_data.dict(exclude_unset=True).items()}
    await db.update_one({"_id": ObjectId(customer_id)}, {"$set": update_data})

    # Retrieve the updated customer
    updated_customer = await db.customers.find_one({"_id": ObjectId(customer_id)})

    return Customer(**updated_customer)

# Delete a customer
async def delete_customer_from_db(customer_id: str):
    

    # Fetch the customer to delete
    existing_customer = await get_customer_by_id(customer_id)
    if not existing_customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Delete the customer from the database
    await db.customers.delete_one({"_id": ObjectId(customer_id)})

    return {"message": "Customer deleted successfully"}

# Get all customers
async def get_all_customers(db: Collection):
    
    customers_cursor = db.customers.find({})
    customers = [Customer(**customer) async for customer in customers_cursor]
    return customers
