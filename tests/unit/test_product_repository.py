import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.base import Base
from src.models.product import Product
from src.repositories.product_repository import ProductRepository
from decimal import Decimal


engine = create_engine("sqlite:///:memory:")
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()


def test_add_product(session):
    repo = ProductRepository(session)

    product = Product(
        name="Test Product",
        description="Test Desc",
        price=Decimal("100"),
        sku="TEST123"
    )

    repo.add(product)
    session.commit()

    result = repo.get_by_id(product.id)
    assert result is not None
    assert result.name == "Test Product"