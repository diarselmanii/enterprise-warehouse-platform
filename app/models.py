from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    sku: str = Field(min_length=3, max_length=50)
    quantity: int = Field(ge=0)
    price: float = Field(gt=0)


class ProductUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    sku: str = Field(min_length=3, max_length=50)
    quantity: int = Field(ge=0)
    price: float = Field(gt=0)


class Product(ProductCreate):
    id: int
