from typing import Optional, List
from src.models.category import Category
from src.unit_of_work.sql_unit_of_work import SQLUnitOfWork


class CategoryService:

    def create_category(self, data: dict) -> Category:
        uow = SQLUnitOfWork()
        try:
            category = Category(**data)
            uow.categories.add(category)
            uow.commit()
            return category
        except Exception:
            uow.rollback()
            raise
        finally:
            uow.dispose()

    def get_category(self, category_id: str) -> Optional[Category]:
        uow = SQLUnitOfWork()
        try:
            return uow.categories.get_by_id(category_id)
        finally:
            uow.dispose()

    def get_categories(self, skip: int = 0, limit: int = 10) -> List[Category]:
        uow = SQLUnitOfWork()
        try:
            return uow.categories.get_all(skip, limit)
        finally:
            uow.dispose()

    def update_category(self, category_id: str, data: dict) -> Optional[Category]:
        uow = SQLUnitOfWork()
        try:
            existing = uow.categories.get_by_id(category_id)
            if not existing:
                return None

            existing.name = data.get("name", existing.name)
            existing.description = data.get("description", existing.description)

            uow.commit()
            return existing
        except Exception:
            uow.rollback()
            raise
        finally:
            uow.dispose()

    def delete_category(self, category_id: str) -> bool:
        uow = SQLUnitOfWork()
        try:
            result = uow.categories.delete(category_id)
            if result:
                uow.commit()
            return result
        except Exception:
            uow.rollback()
            raise
        finally:
            uow.dispose()