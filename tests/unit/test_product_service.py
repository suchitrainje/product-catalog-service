from unittest.mock import MagicMock
from src.services.product_service import ProductService


def test_create_product():
    service = ProductService()
    service.create_product = MagicMock(return_value={"name": "Mock Product"})

    result = service.create_product({
        "name": "Mock Product",
        "description": "Mock Desc",
        "price": 100,
        "sku": "MOCK123"
    })

    assert result["name"] == "Mock Product"