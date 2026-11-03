from fastapi import FastAPI
from app.api.routes import router as products_router

app = FastAPI(
    title="Enterprise Warehouse Platform",
    description="Enterprise Warehouse Management API",
    version="1.0.0"
)

app.include_router(products_router)


@app.get("/")
def root():
    return {
	"message": "Enterprise Warehouse Platform API",
	"status": "running"
    }


@app.get("/health")
def health_check():
    return {
	"status": "healthy",
	"service": "warehouse-api"
    }
