import os

# MongoDB configuration settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")  # Default URI for local MongoDB
DATABASE_NAME = os.getenv("DATABASE_NAME", "umusarurohub")     # Default database name
