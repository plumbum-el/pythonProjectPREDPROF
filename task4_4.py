"""
Решение задачи 4 предпрофессионального экзамена.
Программа читает файл с данными, для каждого продукта и  генерирует промокоды для продуктов
Новые данные сохраняются в файл csv.
В программе реализованы функции:
generate_promo - для преобразования названия продукта в промокод нужного формата

"""

from random import shuffle, sample
from csv import reader, writer


def generate_promo(string):
    """
 “Напитки;Напитки для здоровья;12.06.2022;297.0;25.0” →
 “Напитки;Напитки для здоровья;12.06.2022;297.0;25.0;НА12ЯЬ60”
    """
    name = string.split()
    login = name[0] + '_' + name[1][0]
    if len(name) > 2:
        login += name[2][0]
    return login


with open('products.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    product_data = list(reader(data_file, delimiter=','))
    # Строка с заголовками столбцов
    header_line = product_data.pop(0)

for pupil in product_data:
    # Создать промокод
    promo = generate_promo(pupil[1])
    pupil.append(promo)


with open('products_new.csv', 'w', encoding='utf-8') as data_file:
    data_writer = writer(data_file, delimiter=',')
    # Добавить подписи новых столбцов в строку заголовка
    header_line.append('promo')
    # записать данные в файл
    data_writer.writerows(product_data)