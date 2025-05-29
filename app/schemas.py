"""
This model contains some generic types/schemas for you to use if you wish.

OR you can design your own.
"""

from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class ProductBase(BaseModel):
    """Generic base class of Schema product."""

    name: str
    description: str
    price: float
    category: str
    stock: int


class ProductCreate(ProductBase):
    """Inherits from `ProductBase` however allows for seperation of `Create` models.
    Futureproofing.
    """

    pass


class Product(ProductBase):
    """Inherits from `ProductBase`. But matches the `Product` model from database."""

    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)


class CategoryStats(BaseModel):
    category: str
    product_count: int
    avg_price: float
    min_price: float
    max_price: float
    model_config = ConfigDict(from_attributes=True)
