import uuid
from sqlalchemy import Column, String, Text, DECIMAL, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base
from .product_category import product_categories

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    sku = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    categories = relationship(
        "Category",
        secondary=product_categories,
        back_populates="products"
    )
