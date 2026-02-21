from sqlalchemy.orm import Session
from typing import List, Optional
from src.models.category import Category
from .base_repository import IRepository

class CategoryRepository(IRepository[Category]):

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, item_id: str) -> Optional[Category]:
        return self.session.query(Category).filter(Category.id == item_id).first()

    def get_all(self, skip: int = 0, limit: int = 10) -> List[Category]:
        return self.session.query(Category).offset(skip).limit(limit).all()

    def add(self, item: Category) -> Category:
        self.session.add(item)
        return item

    def update(self, item_id: str, item: Category) -> Optional[Category]:
        db_item = self.get_by_id(item_id)
        if not db_item:
            return None

        db_item.name = item.name
        db_item.description = item.description

        return db_item

    def delete(self, item_id: str) -> bool:
        db_item = self.get_by_id(item_id)
        if not db_item:
            return False

        self.session.delete(db_item)
        return True
