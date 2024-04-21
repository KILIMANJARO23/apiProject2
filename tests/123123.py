###                                                 АВТОЗАПРОС ИЗ ПОСТМАНА

# import requests
#
# url = "https://krasnodar.220-volt.ru/tracker_advcake/"
#
# payload = "{\"pageType\": 3}\r\n"
# headers = {
#   'Content-Type': 'application/json; charset=UTF-8',
#   'Cookie': 'chkuidsrv=35e2ca3a69fa466aadf3bed420a32884; advref=brand_search:google-; advref_first=brand_search:google-; site_version=desktop; client_timestamp=1713694723; session=A53WpsneRNDlDxriGk0KwP; _ym_uid=1713694724702729101; _ym_d=1713694724; _ym_isad=1; _ym_visorc=b; rrpvid=193305643933410; _userGUID=0:lv9dlcf2:lqtGUaow4jPmGOT6DWkBwjmJ9aj_UfTc; rcuid=65c2400c014b856547d52ad5; _gcl_au=1.1.1187061320.1713694725; _ga=GA1.1.1012464355.1713694725; _ga=GA1.3.1012464355.1713694725; _gid=GA1.3.1448785252.1713694725; dSesn=7cef0071-65b0-f519-bb13-043de217e690; _dvs=0:lv9dlcf2:ZAq1BQvMxEd7pJqO5i3hUjDWuGcxTJK9; digi_uc=W1siY3YiLCIyOTA1ODYiLDE3MTM2OTQ4NTQ0MjRdLFsiY3YiLCI3MzUyMjkiLDE3MTM2OTQ4NjU4NTZdXQ==; _gali=city-list-modal; telemetryToken=A53WpsneRNDlDxriGk0KwPreET6ZpsSS1Cdy67F2ouEV; backendStart=1713695493811; backendEnd=1713695494308; system_id=bb91d90a3a2cf59b90128b1d15280596z1713695493; _ga_SFTLJVK4S7=GS1.1.1713694725.1.1.1713695493.60.0.0; backendEnd=1713695647691; backendStart=1713695647631; chkuidsrv=35e2ca3a69fa466aadf3bed420a32884; client_timestamp=1713695064; session=4Ut5CIDtrv8XuCgjHv5XKU; site_version=desktop; system_id=f7602b15da0e1e257c95ed3ac17765d6z1713695647; telemetryToken=A53WpsneRNDlDxriGk0KwPUSLrqv0emoDdOl3BaPqhFv'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)
###                                                 РАСКИДЫВАЕМ КУКИ В СЛОВАРЬ
# # cookie_string = 'Cookie: chkuidsrv=35e2ca3a69fa466aadf3bed420a32884; advref=brand_search:google-; advref_first=brand_search:google-; site_version=desktop; client_timestamp=1713694723; session=A53WpsneRNDlDxriGk0KwP; _ym_uid=1713694724702729101; _ym_d=1713694724; _ym_isad=1; _ym_visorc=b; rrpvid=193305643933410; _userGUID=0:lv9dlcf2:lqtGUaow4jPmGOT6DWkBwjmJ9aj_UfTc; rcuid=65c2400c014b856547d52ad5; _gcl_au=1.1.1187061320.1713694725; _ga=GA1.1.1012464355.1713694725; _ga=GA1.3.1012464355.1713694725; _gid=GA1.3.1448785252.1713694725; dSesn=7cef0071-65b0-f519-bb13-043de217e690; _dvs=0:lv9dlcf2:ZAq1BQvMxEd7pJqO5i3hUjDWuGcxTJK9; digi_uc=W1siY3YiLCIyOTA1ODYiLDE3MTM2OTQ4NTQ0MjRdLFsiY3YiLCI3MzUyMjkiLDE3MTM2OTQ4NjU4NTZdXQ==; _gali=city-list-modal; telemetryToken=A53WpsneRNDlDxriGk0KwPreET6ZpsSS1Cdy67F2ouEV; backendStart=1713695493811; backendEnd=1713695494308; system_id=bb91d90a3a2cf59b90128b1d15280596z1713695493; _ga_SFTLJVK4S7=GS1.1.1713694725.1.1.1713695493.60.0.0; backendEnd=1713697123832; backendStart=1713697123713; chkuidsrv=35e2ca3a69fa466aadf3bed420a32884; client_timestamp=1713695064; session=4Ut5CIDtrv8XuCgjHv5XKU; site_version=desktop; system_id=98940d66283f61f3a30400baee3398f1z1713697123; telemetryToken=A53WpsneRNDlDxriGk0KwPt7mlu3ih5tt1Iwm4n9v0KL'
# #
# # # Удаляем префикс 'Cookie: '
# # cookie_string = cookie_string.replace('Cookie: ', '')
# #
# # # Разделяем куки на отдельные куки
# # cookies = cookie_string.split(';')
# #
# # # Создаем словарь куков
# # cookie_dict = {}
# # for cookie in cookies:
# #     # Удаляем пробелы вокруг куков
# #     cookie = cookie.strip()
# #     # Разделяем куки на ключ и значение
# #     key, value = cookie.split('=', 1)
# #     # Добавляем куки в словарь
# #     cookie_dict[key] = value
# #
# # print(cookie_dict)
###                                                         ПАРСИМ HTML
# from bs4 import BeautifulSoup
# import requests
#
# # URL страницы, с которой вы хотите извлечь информацию
# url = 'https://krasnodar.220-volt.ru/catalog/benzopily/hyundai/'
#
# # Отправляем запрос к странице
# response = requests.get(url)
#
# # Проверяем, что запрос прошёл успешно
# if response.status_code == 200:
#   # Создаем объект BeautifulSoup
#   soup = BeautifulSoup(response.text, 'html.parser')
#
#   # Ищем все элементы с классом 'new-item-list-price-im'
#   price_elements = soup.find_all(class_='new-item-list-price-im')
#
#   # Перебираем найденные элементы и извлекаем текст
#   for price_element in price_elements:
#     price = price_element.get_text()
#     print(price)
# else:
#   print('Failed to retrieve the webpage')

###                                                 ПАЙДАНТИК МОДЕЛЬ. ПРИМЕР
# from typing import List
# from pydantic import BaseModel, ValidationError
#
# # Определяем модель для продукта
# class Product(BaseModel):
#     id: str
#     name: str
#
# # Определяем модель для списка продуктов
# class Products(BaseModel):
#     products: List[Product]
#
# # Пример данных продуктов
# product_data = [
#     {'name': 'Бензопила HYUNDAI Х 5320', 'id': '735229'},
#     {'id': '735227', 'name': 'Бензопила HYUNDAI Х 3916'},
#     {'id': '735228', 'name': 'Бензопила HYUNDAI Х 4118'},
#     {'id': '697556', 'name': 'Бензопила HYUNDAI X 520'},
#     {'name': 'Бензопила HYUNDAI X 420', 'id': '697555'},
#     {'id': '697554', 'name': 'Бензопила HYUNDAI X 370'}
# ]
#
# # Проверяем данные продуктов
# try:
#     products = Products(products=product_data)
#     print(products.dict())
#     print("Проверка типов данных прошла успешно.")
# except ValidationError as e:
#     print(e.json())
###                                 Достаём из ответа сервера информацию о категориях
# import json
#
# # Предположим, что у вас есть JSON-строка в переменной json_string
# json_string = '''
# {
#     "user": {
#         "email": "fbdb1d1b18aa6c08324b7d64b71fb76370690e1d"
#     },
#     "currentCategory": {
#         "name": "Сад и дача",
#         "id": 339
#     },
#     "products": [
#         {
#             "id": "735229",
#             "name": "Бензопила HYUNDAI Х 5320"
#         },
#         {
#             "name": "Бензопила HYUNDAI Х 3916",
#             "id": "735227"
#         },
#         {
#             "name": "Бензопила HYUNDAI Х 4118",
#             "id": "735228"
#         },
#         {
#             "name": "Бензопила HYUNDAI X 520",
#             "id": "697556"
#         },
#         {
#             "id": "697555",
#             "name": "Бензопила HYUNDAI X 420"
#         },
#         {
#             "name": "Бензопила HYUNDAI X 370",
#             "id": "697554"
#         }
#     ],
#     "basketProducts": [],
#     "pageType": 3
# }
# '''
#
# # Десериализуем JSON-строку в объект Python
# data = json.loads(json_string)
#
# # Извлекаем значения "products"
# products = data['products']
#
# # Теперь products - это список словарей, каждый из которых представляет собой продукт
# # for product in products:
# #     print(product)
# print(products)

# import re
#
# # Ваш список словарей
# products = [
#     {'name': 'Бензопила HYUNDAI Х 5320', 'id': '735229'},
#     {'id': '735227', 'name': 'Бензопила HYUNDAI Х 3916'},
#     {'id': '735228', 'name': 'Бензопила HYUNDAI Х 4118'},
#     {'id': '697556', 'name': 'Бензопила HYUNDAI X 520'},
#     {'name': 'Бензопила HYUNDAI X 420', 'id': '697555'},
#     {'id': '697554', 'name': 'Бензопила HYUNDAI X 370'}
# ]
#
# # Регулярное выражение для поиска и удаления "Бензопила HYUNDAI"
# pattern = r"Бензопила HYUNDAI "
#
# # Проход по каждому словарю в списке и удаление "Бензопила HYUNDAI"
# for product in products:
#     for key in product:
#         product[key] = re.sub(pattern, '', product[key])
#
# # Вывод обновленного списка
# print(products)

