from fastapi import APIRouter, HTTPException, status
from app.models import Product, ProductCreate, ProductUpdate

router = APIRouter(prefix="/products", tags=["Products"])

#Temporary in-memory storage
products = {}
next_product_id = 1


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    global next_product_id

    for existing_product in products.values():
    if existing_product["sku"] == product.sku:
        raise HTTPException(
            status_code=409,
            detail="Product SKU already exists"
        )

    new_product = {
        "id": next_product_id,
        **product.model_dump()
    }

    products[next_product_id] = new_product
    next_product_id += 1

    return new_product


@router.get("/", response_model=list[Product])
def get_products():
    return list(products.values())


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = products.get(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: ProductUpdate):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    for existing_id, existing_product in products.items():
        if existing_id != product_id and existing_product["sku"] == updated_product.sku:
           raise HTTPException(
               status_code=409,
               detail="Product SKU already exists"
           )

    products[product_id] = {
        "id": product_id,
        **updated_product.model_dump()
    }

    return products[product_id]


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    del products[product_id]
