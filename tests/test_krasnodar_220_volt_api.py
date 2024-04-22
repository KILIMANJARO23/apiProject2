import allure
from utils.checking import Checking
from utils.api import Krasnodar220VoltApi

"""Получения информации о категории и продуктах"""

@allure.epic("Test test take category and product list")
class TestTakeCategoryAndProductList():

    @allure.description("Test take category and product list")
    def test_take_category_and_product_list(self):
        print("Метод POST")
        result_post = Krasnodar220VoltApi.category_and_product_list()
        Checking.check_status_code(result_post, 200)






