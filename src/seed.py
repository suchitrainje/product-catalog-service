from src.database import SessionLocal
from src.models.product import Product
from src.models.category import Category
from decimal import Decimal


def seed_database():
    session = SessionLocal()

    # Check if already seeded
    if session.query(Category).first():
        session.close()
        return

    # Create categories
    electronics = Category(name="Electronics", description="Electronic items")
    fashion = Category(name="Fashion", description="Clothing and accessories")
    books = Category(name="Books", description="All kinds of books")

    session.add_all([electronics, fashion, books])
    session.commit()

    # Create products
    products = [
        Product(name="Laptop", description="Gaming laptop", price=Decimal("75000"), sku="SKU001", categories=[electronics]),
        Product(name="Mobile", description="Smartphone", price=Decimal("30000"), sku="SKU002", categories=[electronics]),
        Product(name="T-Shirt", description="Cotton T-Shirt", price=Decimal("999"), sku="SKU003", categories=[fashion]),
        Product(name="Jeans", description="Denim jeans", price=Decimal("1999"), sku="SKU004", categories=[fashion]),
        Product(name="Novel", description="Fiction novel", price=Decimal("499"), sku="SKU005", categories=[books]),
        Product(name="Headphones", description="Bluetooth headphones", price=Decimal("2500"), sku="SKU006", categories=[electronics]),
        Product(name="Shoes", description="Running shoes", price=Decimal("3500"), sku="SKU007", categories=[fashion]),
        Product(name="Keyboard", description="Mechanical keyboard", price=Decimal("4500"), sku="SKU008", categories=[electronics]),
        Product(name="Backpack", description="Travel backpack", price=Decimal("1800"), sku="SKU009", categories=[fashion]),
        Product(name="Notebook", description="Spiral notebook", price=Decimal("120"), sku="SKU010", categories=[books]),
    ]

    session.add_all(products)
    session.commit()
    session.close()