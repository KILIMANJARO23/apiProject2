from utils.http_methods import HttpMethod
from typing import List
from pydantic import BaseModel, ValidationError
import re
import pandas as pd

"""Методы для тестирования Krasnodar220VoltApi"""

base_url = "https://krasnodar.220-volt.ru/tracker_advcake/"        #базовая url
headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Cookie': 'chkuidsrv=35e2ca3a69fa466aadf3bed420a32884; advref=brand_search:google-; advref_first=brand_search:google-; site_version=desktop; client_timestamp=1713694723; session=A53WpsneRNDlDxriGk0KwP; _ym_uid=1713694724702729101; _ym_d=1713694724; _ym_isad=1; _ym_visorc=b; rrpvid=193305643933410; _userGUID=0:lv9dlcf2:lqtGUaow4jPmGOT6DWkBwjmJ9aj_UfTc; rcuid=65c2400c014b856547d52ad5; _gcl_au=1.1.1187061320.1713694725; _ga=GA1.1.1012464355.1713694725; _ga=GA1.3.1012464355.1713694725; _gid=GA1.3.1448785252.1713694725; dSesn=7cef0071-65b0-f519-bb13-043de217e690; _dvs=0:lv9dlcf2:ZAq1BQvMxEd7pJqO5i3hUjDWuGcxTJK9; digi_uc=W1siY3YiLCIyOTA1ODYiLDE3MTM2OTQ4NTQ0MjRdLFsiY3YiLCI3MzUyMjkiLDE3MTM2OTQ4NjU4NTZdXQ==; _gali=city-list-modal; telemetryToken=A53WpsneRNDlDxriGk0KwPreET6ZpsSS1Cdy67F2ouEV; backendStart=1713695493811; backendEnd=1713695494308; system_id=bb91d90a3a2cf59b90128b1d15280596z1713695493; _ga_SFTLJVK4S7=GS1.1.1713694725.1.1.1713695493.60.0.0; backendEnd=1713695647691; backendStart=1713695647631; chkuidsrv=35e2ca3a69fa466aadf3bed420a32884; client_timestamp=1713695064; session=4Ut5CIDtrv8XuCgjHv5XKU; site_version=desktop; system_id=f7602b15da0e1e257c95ed3ac17765d6z1713695647; telemetryToken=A53WpsneRNDlDxriGk0KwPUSLrqv0emoDdOl3BaPqhFv'
}   #Хэдеры для всех запросов


class Krasnodar220VoltApi():

    """Метод для получения списка бензопил марки HYUNDAI"""

    @staticmethod
    def category_and_product_list():

        json_for_category_and_product_list = {"pageType": 3}

        post_url = base_url
        print(post_url)
        result_post = HttpMethod.post(post_url, json_for_category_and_product_list)
        print(result_post.text)  # Получаем ответ от сервера в текстовом (string) формате
        data = result_post.json() # Присваиваем переменной data значение в JSON, которое возвращает сервер
        products = data['products']
        print(products)



        """Верификация данных через Pydantic модель"""
        # Определяем модель для продукта
        class Product(BaseModel):
            id: str
            name: str

        # Определяем модель для списка продуктов
        class Products(BaseModel):
            products: List[Product]

        # Пример данных продуктов
        products

        # Проверяем данные продуктов
        try:
            products1 = Products(products=products)
            print(products1.dict())
            print("Проверка типов данных прошла успешно.")
        except ValidationError as e:
            print(e.json())



        """Регулярное выражение для поиска и удаления "Бензопила HYUNDAI"""

        pattern = r"Бензопила HYUNDAI "

        # Проход по каждому словарю в списке и удаление "Бензопила HYUNDAI"
        for product in products:
            for key in product:
                product[key] = re.sub(pattern, '', product[key])

        # Вывод обновленного списка
        print(products)


        """Создание Excel файла c укороченными названиями моделей бензопил и их id"""
        # Создаем DataFrame из списка
        df = pd.DataFrame(products)

        # Записываем DataFrame в Excel файл
        df.to_excel('C:\\Users\\volch\\PycharmProjects\\apiProject2\\Бензопилы.xlsx', index=False)

        print("Данные успешно записаны в файл 'Бензопилы.xlsx'")

        return result_post

