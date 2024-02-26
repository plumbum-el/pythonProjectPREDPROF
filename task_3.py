"""
Решение задачи 3 предпрофессионального экзамена.
Программа читает данные из файла.
Далее в бесконечном цикле запрашивает название категории и
ищет его линейным поиском.
Выход из цикла - по значению "молоко"
"""

from csv import reader

with open('products.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    products_data = list(reader(data_file, delimiter=','))
# Ввод первого значения
category = input('Введите название категории или "молоко": ')
# Цикл до ввода молоко
while category != 'молоко':
    # Линейный поиск позиции искомого значения
    position = -1
    for i in range(len(products_data)):
        if products_data[i][0] == category:
            position = i
            break
    # Вывод на экран
    if position >= 0:
        product = products_data[position][0].split()
        name = product[0] + '.' + product[0]
        print(f'Категория {category} товар: {name} был куплен - {products_data[position][-1]} раз.')
    else:
        print('Такой категории не существует в нашей БД')
    # Чтение следующего значения
    category = input('Введите название категории или "молоко": ')