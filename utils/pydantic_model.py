# from pydantic import BaseModel, ValidationError
# from typing import List
#
#
# """Верификация данных через Pydantic модель"""
#         # Определяем модель для продукта
#         class Product(BaseModel):
#             id: str
#             name: str
#
#         # Определяем модель для списка продуктов
#         class Products(BaseModel):
#             products: List[Product]
#
#         # Пример данных продуктов
#         products
#
#         # Проверяем данные продуктов
#         try:
#             products1 = Products(products=products)
#             print(products1.dict())
#             print("Проверка типов данных прошла успешно.")
#         except ValidationError as e:
#             print(e.json())

# from pydantic import BaseModel, ValidationError
# from typing import List
#
# class Product(BaseModel):
#     id: str
#     name: str
#
# class Products(BaseModel):
#     products: List[Product]
#
# def validate_products(products):
#     try:
#         products1 = Products()
#         print(products1.dict())
#         print("Проверка типов данных прошла успешно.")
#     except ValidationError as e:
#         print(e.json())

from pydantic import BaseModel, ValidationError
from typing import List, Type, Any

class Product(BaseModel):
    id: str
    name: str

class Products(BaseModel):
    products: List[Product]

def validate_data(data: Any, model: Type[BaseModel]):
    try:
        validated_data = model(**data)
        print(validated_data.dict())
        print("Проверка типов данных прошла успешно.")
    except ValidationError as e:
        print(e.json())
