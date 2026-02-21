from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from src.models.product import Product
from src.models.category import Category
from .base_repository import IRepository


class ProductRepository(IRepository[Product]):

    def __init__(self, session: Session):
        self.session = session

    # ----------------------
    # BASIC CRUD OPERATIONS
    # ----------------------

    def get_by_id(self, item_id: str) -> Optional[Product]:
        return self.session.query(Product).filter(Product.id == item_id).first()

    def get_all(self, skip: int = 0, limit: int = 10) -> List[Product]:
        return (
            self.session.query(Product)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def add(self, item: Product) -> Product:
        self.session.add(item)
        return item

    def update(self, item_id: str, item: Product) -> Optional[Product]:
        db_item = self.get_by_id(item_id)
        if not db_item:
            return None

        db_item.name = item.name
        db_item.description = item.description
        db_item.price = item.price
        db_item.sku = item.sku

        return db_item

    def delete(self, item_id: str) -> bool:
        db_item = self.get_by_id(item_id)
        if not db_item:
            return False

        self.session.delete(db_item)
        return True

    # ----------------------
    # ADVANCED SEARCH
    # ----------------------

    def search(
        self,
        q: Optional[str] = None,
        category_id: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        skip: int = 0,
        limit: int = 10
    ) -> List[Product]:

        query = self.session.query(Product)

        # Keyword search (name + description)
        if q:
            query = query.filter(
                or_(
                    Product.name.ilike(f"%{q}%"),
                    Product.description.ilike(f"%{q}%")
                )
            )

        # Category filter
        if category_id:
            query = query.join(Product.categories).filter(Category.id == category_id)

        # Price filters
        if min_price is not None:
            query = query.filter(Product.price >= min_price)

        if max_price is not None:
            query = query.filter(Product.price <= max_price)

        return query.offset(skip).limit(limit).all()
