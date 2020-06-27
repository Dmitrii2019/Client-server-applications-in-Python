import csv
import re

'''
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из
файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
«отчетный» файл в формате CSV.
Для этого:
* Создать функцию get_data(), в которой в цикле осуществляется
перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных
выражений извлечь значения параметров «Изготовитель системы», «Название ОС»,
«Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например,
os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в
файл main_data (также для каждого файла);
'''


fails = ['info_1', 'info_2', 'info_3']
fails2 = [['Изготовитель системы',
           'Название ОС',
           'Код продукта',
           'Тип системы']]

with open('main_data.csv', 'w') as f_n1:
    f_n_writer = csv.writer(f_n1, quoting=csv.QUOTE_NONNUMERIC)
    for row in fails2:
        f_n_writer.writerow(row)


def get_data():
    for info in fails:
        with open(f'{info}.txt', encoding='cp1251') as f_n:
            for el_str in f_n:
                result = re.findall(r'^Изготовитель системы:\s*(.*)$', el_str)
                if result:
                    os_prod_list = result

                result1 = re.findall(r'^Название ОС:\s*(.*)$', el_str)
                if result1:
                    os_name_list = result1

                result2 = re.findall(r'^Код продукта:\s*(.*)$', el_str)
                if result2:
                    os_code_list = result2

                result3 = re.findall(r'^Тип системы:\s*(.*)$', el_str)
                if result3:
                    os_type_list = result3

            data = [[os_prod_list, os_name_list, os_code_list, os_type_list]]

            with open('main_data.csv', 'a') as f_n1:
                f_n_writer = csv.writer(f_n1, quoting=csv.QUOTE_NONNUMERIC)
                for row in data:
                    f_n_writer.writerow(row)


get_data()
