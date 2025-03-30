from fastapi import FastAPI
from routes.customer_routes import router as customer_router

app = FastAPI()

app.include_router(customer_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al sistema de atención al cliente del banco."}