from fastapi import FastAPI, HTTPException, status
from typing import Optional, List

from src.services.product_service import ProductService
from src.services.category_service import CategoryService

from src.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)
from src.schemas.category_schema import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse
)

from src.database import engine
from src.models.base import Base
from src.seed import seed_database


app = FastAPI(title="Product Catalog Service")

product_service = ProductService()
category_service = CategoryService()


# =========================================================
# STARTUP EVENT (Create tables + Seed DB)
# =========================================================
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    seed_database()


# =========================================================
# HEALTH CHECK
# =========================================================
@app.get("/health")
def health():
    return {"status": "UP"}


# =========================================================
# PRODUCT ENDPOINTS
# =========================================================

# CREATE PRODUCT
@app.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    return product_service.create_product(product.dict())


# GET SINGLE PRODUCT
@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: str):
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# GET ALL PRODUCTS (Pagination)
@app.get("/products", response_model=List[ProductResponse])
def get_products(skip: int = 0, limit: int = 10):
    return product_service.get_products(skip, limit)


# UPDATE PRODUCT
@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: str, product: ProductUpdate):
    updated = product_service.update_product(
        product_id,
        product.dict(exclude_unset=True)
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


# DELETE PRODUCT
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: str):
    result = product_service.delete_product(product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return


# ADVANCED SEARCH
@app.get("/products/search", response_model=List[ProductResponse])
def search_products(
    q: Optional[str] = None,
    category_id: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    skip: int = 0,
    limit: int = 10
):
    return product_service.search_products(
        q=q,
        category_id=category_id,
        min_price=min_price,
        max_price=max_price,
        skip=skip,
        limit=limit
    )


# =========================================================
# CATEGORY ENDPOINTS
# =========================================================

# CREATE CATEGORY
@app.post("/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate):
    return category_service.create_category(category.dict())


# GET SINGLE CATEGORY
@app.get("/categories/{category_id}", response_model=CategoryResponse)
def get_category(category_id: str):
    category = category_service.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


# GET ALL CATEGORIES
@app.get("/categories", response_model=List[CategoryResponse])
def get_categories(skip: int = 0, limit: int = 10):
    return category_service.get_categories(skip, limit)


# UPDATE CATEGORY
@app.put("/categories/{category_id}", response_model=CategoryResponse)
def update_category(category_id: str, category: CategoryUpdate):
    updated = category_service.update_category(
        category_id,
        category.dict(exclude_unset=True)
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated


# DELETE CATEGORY
@app.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: str):
    result = category_service.delete_category(category_id)
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return