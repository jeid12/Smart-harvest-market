from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
import os

# Initialize the database connection
try:
    mongo_uri = os.getenv( "mongodb://localhost:27017")
    client = AsyncIOMotorClient(mongo_uri)
    db = client.get_database("umusarurohub")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    raise

# Dependency to provide the database
def get_db():
    return db
