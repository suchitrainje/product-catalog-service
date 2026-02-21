from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from decimal import Decimal


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    sku: str
    category_ids: Optional[List[UUID]] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    sku: Optional[str] = None
    category_ids: Optional[List[UUID]] = None


class ProductResponse(ProductBase):
    id: UUID

    class Config:
        orm_mode = True
