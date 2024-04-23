import pandas as pd

def export_to_excel(data):
    filename = 'C:\\Users\\volch\\PycharmProjects\\apiProject2\\Бензопилы.xlsx'

    # Создаем DataFrame из списка
    df = pd.DataFrame(data)

    # Записываем DataFrame в Excel файл
    df.to_excel(filename, index=False)

    print(f"Данные успешно записаны в файл '{filename}'")
