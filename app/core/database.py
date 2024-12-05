from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
from pymongo.collection import Collection
import os

# Initialize the database connection
client = AsyncIOMotorClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client.get_database("umusarurohub")

def get_db():
    return db
