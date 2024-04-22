import allure
from utils.checking import Checking
from utils.api import Krasnodar220VoltApi
from utils.pydantic_model import validate_data
from utils.pydantic_model import Products


"""Получения информации о категории и продуктах"""

@allure.epic("Test test take category and product list")
class TestTakeCategoryAndProductList():

    @allure.description("Test take category and product list")
    def test_take_category_and_product_list(self):
        print("Метод POST")
        result_post = Krasnodar220VoltApi.category_and_product_list()
        Checking.check_status_code(result_post, 200)

    def test_validate_data(self):
        validate_data(Krasnodar220VoltApi.category_and_product_list().json(), Products)








