import allure
from utils.checking import Checking
from utils.api import Krasnodar220VoltApi
from utils.pydantic_model import validate_data
from utils.pydantic_model import Products
from utils.regular_expression import RegularExpressions

"""Получения информации о категории и продуктах"""

@allure.epic("Test test take category and product list")
class TestTakeCategoryAndProductList():

    @allure.description("Test take category and product list")
    def test_take_category_and_product_list(self):
        print("Метод POST")
        result_post = Krasnodar220VoltApi.category_and_product_list()
        """Проверка статус кода"""
        Checking.check_status_code(result_post, 200)
        """Валидация данных с помощью Pydantic"""
        validate_data(result_post.json(), Products)
        """Срез с помощью регулярных выражений"""
        RegularExpressions.creating_a_slice(result_post.json()["products"])










