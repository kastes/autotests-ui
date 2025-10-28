from typing import TypedDict
from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Цена больше 0!")
    tags: list[str]
    market: Market


product1 = Product(name="phone", price=499.99, tags=["electronics", "smartphones"], market=Market(id=1, name="Ozon"))
print(product1)
print()

product2 = Product(name="keyboard", price=4.99, tags=["electronics", "devices"], market=Market(id=2, name="DNS"))
print(product2)
print()


# mypy проверяет статически, pydantic при выполнении
# поэтому для mypy используем TypedDict
class MarketData(TypedDict):
    id: int
    name: str


class ProductData(TypedDict):
    name: str
    price: float
    tags: list[str]
    market: Market


market_data: MarketData = {"name": "Portal", "id": 3}
market = Market(**market_data)
product_data: ProductData = {"name": "mouse", "price": 10.50, "tags": ["electronics", "devices"], "market": market}
product3 = Product(**product_data)
print(product3)
print()

product4 = Product(name="keyboard", price=0, tags=["electronics", "devices"], market=Market(id=2, name="DNS"))
print(product4)
print()
