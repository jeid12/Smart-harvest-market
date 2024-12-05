from fastapi import FastAPI
from controllers.farmer_controller import router as farmer_router

app = FastAPI()

app.include_router(farmer_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Farmer's Market API!"}
