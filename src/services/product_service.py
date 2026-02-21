from typing import Optional, List
from src.models.product import Product
from src.models.category import Category
from src.unit_of_work.sql_unit_of_work import SQLUnitOfWork


class ProductService:

    # -----------------------
    # CREATE PRODUCT
    # -----------------------
    def create_product(self, data: dict) -> Product:
        uow = SQLUnitOfWork()
        try:
            product = Product(
                name=data["name"],
                description=data.get("description"),
                price=data["price"],
                sku=data["sku"]
            )

            # Assign categories if provided
            if "category_ids" in data:
                for category_id in data["category_ids"]:
                    category = uow.categories.get_by_id(category_id)
                    if category:
                        product.categories.append(category)

            uow.products.add(product)
            uow.commit()
            return product

        except Exception:
            uow.rollback()
            raise
        finally:
            uow.dispose()

    # -----------------------
    # GET SINGLE PRODUCT
    # -----------------------
    def get_product(self, product_id: str) -> Optional[Product]:
        uow = SQLUnitOfWork()
        try:
            return uow.products.get_by_id(product_id)
        finally:
            uow.dispose()

    # -----------------------
    # GET ALL PRODUCTS
    # -----------------------
    def get_products(self, skip: int = 0, limit: int = 10) -> List[Product]:
        uow = SQLUnitOfWork()
        try:
            return uow.products.get_all(skip, limit)
        finally:
            uow.dispose()

    # -----------------------
    # UPDATE PRODUCT
    # -----------------------
    def update_product(self, product_id: str, data: dict) -> Optional[Product]:
        uow = SQLUnitOfWork()
        try:
            existing_product = uow.products.get_by_id(product_id)
            if not existing_product:
                return None

            existing_product.name = data.get("name", existing_product.name)
            existing_product.description = data.get("description", existing_product.description)
            existing_product.price = data.get("price", existing_product.price)
            existing_product.sku = data.get("sku", existing_product.sku)

            # Update categories if provided
            if "category_ids" in data:
                existing_product.categories.clear()
                for category_id in data["category_ids"]:
                    category = uow.categories.get_by_id(category_id)
                    if category:
                        existing_product.categories.append(category)

            uow.commit()
            return existing_product

        except Exception:
            uow.rollback()
            raise
        finally:
            uow.dispose()

    # -----------------------
    # DELETE PRODUCT
    # -----------------------
    def delete_product(self, product_id: str) -> bool:
        uow = SQLUnitOfWork()
        try:
            result = uow.products.delete(product_id)
            if result:
                uow.commit()
            return result
        except Exception:
            uow.rollback()
            raise
        finally:
            uow.dispose()

    # -----------------------
    # ADVANCED SEARCH
    # -----------------------
    def search_products(
        self,
        q: Optional[str] = None,
        category_id: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        skip: int = 0,
        limit: int = 10
    ) -> List[Product]:

        uow = SQLUnitOfWork()
        try:
            return uow.products.search(
                q=q,
                category_id=category_id,
                min_price=min_price,
                max_price=max_price,
                skip=skip,
                limit=limit
            )
        finally:
            uow.dispose()
