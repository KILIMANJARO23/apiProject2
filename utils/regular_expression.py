# import re
#
# """Регулярное выражение для поиска и удаления "Бензопила HYUNDAI"""
#
#         pattern = r"Бензопила HYUNDAI "
#
#         # Проход по каждому словарю в списке и удаление "Бензопила HYUNDAI"
#         for product in products:
#             for key in product:
#                 product[key] = re.sub(pattern, '', product[key])
#
#         # Вывод обновленного списка
#         print(products)


import re

class RegularExpressions():
    def creating_a_slice(products):
        what_to_remove = r"Бензопила HYUNDAI "
        remove_pattern = what_to_remove

        # Проход по каждому словарю в списке и удаление "Бензопила HYUNDAI"
        for product in products:
            for key, value in product.items():
                if isinstance(value, str):  # Проверяем, что значение является строкой
                    product[key] = re.sub(remove_pattern, '', value)

        # Вывод обновленного списка
        print(products)