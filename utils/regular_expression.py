import re

class RegularExpressions():

    """Функция, реализующая срезы"""

    def creating_a_slice(words):

        remove_pattern = r"Бензопила HYUNDAI "

        # Проход по каждому словарю в списке и удаление "Бензопила HYUNDAI"

        for word in words:
            for key, value in word.items():
                if isinstance(value, str):  # Проверяем, что значение является строкой
                    word[key] = re.sub(remove_pattern, '', value)

        # Вывод обновленного списка
        print(words)