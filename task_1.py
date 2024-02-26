from csv import reader, writer

main_total = []
# Выполнение 1-й части задания
with open('products.csv', encoding='utf-8') as data_file:
    # Открыть файл с данными как объект reader
    csv_data = reader(data_file, delimiter=';')
    # Линейным поиском получить ответ
    for row in csv_data:
        total = int(row[3][0:-2:]) * int(row[4][0:-2:])
        main_total.append(total)
        with open('products_new.csv', 'w', encoding='utf-8') as data_file:
        total_write = writer(total)
        # Запись в объект writer
        data_writer = writer(data_file, delimiter=',')
        # Строка с подписями столбцов
        data_writer.writerow(total)
        data_writer.writerows(total_write)


print(sum(main_total))
