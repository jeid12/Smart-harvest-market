from models.customer import CustomerCreate, Customer, CustomerUpdate
from fastapi import HTTPException, Depends
from bson import ObjectId
from core.database import get_db
from pymongo.collection import Collection
from passlib.context import CryptContext

# Initialize CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Get the database dependency
def get_customer_collection(db = Depends(get_db)) -> Collection:
    return db["customers"]

# Create a customer
async def create_customer_in_db(customer_data: CustomerCreate, db: Collection = Depends(get_customer_collection)):
    # Check if a customer with the same email already exists
    existing_customer_by_email = await db.find_one({"email": customer_data.email})
    if existing_customer_by_email:
        raise HTTPException(status_code=400, detail="Email already in use")

    # Check if a customer with the same username already exists
    existing_customer_by_username = await db.find_one({"username": customer_data.username})
    if existing_customer_by_username:
        raise HTTPException(status_code=400, detail="Username already in use")

    # Hash the password before saving it
    hashed_password = pwd_context.hash(customer_data.password)
    customer_data.password = hashed_password

    # Insert the customer data into the MongoDB collection
    result = await db.insert_one(customer_data.dict())

    # Retrieve the customer after insertion to get the MongoDB _id
    created_customer = await db.find_one({"_id": result.inserted_id})

    return Customer(**created_customer)

# Get a customer by ID
async def get_customer_by_id(customer_id: str, db: Collection = Depends(get_customer_collection)):
    return await db.find_one({"_id": ObjectId(customer_id)})

# Get a customer by email
async def get_customer_by_email(email: str, db: Collection = Depends(get_customer_collection)):
    return await db.find_one({"email": email})

# Get a customer by username
async def get_customer_by_username(username: str, db: Collection = Depends(get_customer_collection)):
    return await db.find_one({"username": username})

# Update a customer
async def update_customer_in_db(customer_id: str, customer_data: CustomerUpdate, db: Collection = Depends(get_customer_collection)):
    # Fetch the existing customer to update
    existing_customer = await get_customer_by_id(customer_id, db)
    if not existing_customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # If password is updated, hash it before saving
    if customer_data.password:
        customer_data.password = pwd_context.hash(customer_data.password)

    # Update the customer in the database
    update_data = {key: value for key, value in customer_data.dict(exclude_unset=True).items()}
    await db.update_one({"_id": ObjectId(customer_id)}, {"$set": update_data})

    # Retrieve the updated customer
    updated_customer = await db.find_one({"_id": ObjectId(customer_id)})

    return Customer(**updated_customer)

# Delete a customer
async def delete_customer_from_db(customer_id: str, db: Collection = Depends(get_customer_collection)):
    # Fetch the customer to delete
    existing_customer = await get_customer_by_id(customer_id, db)
    if not existing_customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Delete the customer from the database
    await db.delete_one({"_id": ObjectId(customer_id)})

    return {"message": "Customer deleted successfully"}

# Get all customers
async def get_all_customers(db: Collection = Depends(get_customer_collection)):
    customers_cursor = db.find({})
    customers = [Customer(**customer) async for customer in customers_cursor]
    return customers
