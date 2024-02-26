"""
Решение задачи 2 предпрофессионального экзамена
Программа сортирует по группам в алфавитном порядке категории
товаров в таблице products.csv и в первой категории выводит самый дорогой товар.
Формат вывода: “В категории: <Category> самый дорогой
товар: <product> его цена за единицу товара составляет <Price per unit>”
"""


from csv import reader

with open('products.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    produsts_data = list(reader(data_file, delimiter=','))
    # Строка с подписями столбцов
    header_line = produsts_data.pop(0)
    # Реализация сортировки вставками
    # Первый критерий сортировки - название продукта
    # Второй критерий - цена
    for i in range(1, len(produsts_data)):
        # Текущий элемент
        elem = produsts_data[i]
        # Поиск места вставки и сдвиг всех значений больше текущего
        j = i
        while j > 0 and produsts_data[j - 1][6] > elem[6]:
            produsts_data[j] = produsts_data[j - 1]
            j -= 1
        # Вставка значения
        produsts_data[j] = elem

    for i in range(3):
        pupil_name = produsts_data[-1 - i][1].split()
        name = pupil_name[1][0] + '.' + pupil_name[0]
        print(f'{i + 1} Price per unit: {name}')