from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.farmer_controller import router as farmer_router
from controllers.customer_controller import router as  customer_router
from controllers.warehouse_controller import router as warehouse_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust based on your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(farmer_router,prefix="/farmers",tags=["Farmers"])
app.include_router(customer_router,prefix="/customers",tags=["Customers"])
app.include_router(warehouse_router, prefix="/warehouses", tags=["Warehouses"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Farmer's Market API!"}
