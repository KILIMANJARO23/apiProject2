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
