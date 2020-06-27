import json


'''
2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными.
Для этого:
* Создать функцию write_order_to_json(),
в которую передается 5 параметров —
товар (item),количество (quantity),
цена (price), покупатель (buyer),
дата (date). Функция должна предусматривать запись данных
в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
* Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра
'''


def write_order_to_json(item, quantity, price, buyer, date):

    dict_to_json = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(dict_to_json, f_n, indent=4)


write_order_to_json('Стул комфорт', 5, 5480, 'Anton', '17.06.2020')
