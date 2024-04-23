import re

class RegularExpressions():

    remove_pattern = r"Бензопила HYUNDAI "

    """Функция, реализующая срезы"""

    def creating_a_slice(words):

        # Проход по каждому словарю в списке и удаление "Бензопила HYUNDAI"

        for word in words:
            for key, value in word.items():
                if isinstance(value, str):  # Проверяем, что значение является строкой
                    word[key] = re.sub(RegularExpressions.remove_pattern, '', value)

        # Вывод обновленного списка
        print(words)