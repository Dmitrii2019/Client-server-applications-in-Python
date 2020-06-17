import yaml

'''
3. Задание на закрепление знаний по модулю yaml. Написать скрипт,
автоматизирующий сохранение данных в файле YAML-формата.
Для этого:
* Подготовить данные для записи в виде словаря,
в котором первому ключу соответствует список,
второму — целое число, третьему — вложенный словарь,
где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);
* Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с
помощью параметра default_flow_style, а также установить
возможность работы с юникодом: allow_unicode = True;
* Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
'''


data_yaml = {'data_key1': ['data_value1', 'data_value2'],
             'data_key2': 5, 'data_key3': {'1€': 'data_value_1'}}

with open('file.yaml', 'w') as f_n:
    yaml.dump(data_yaml, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml') as f_n:
    f_n_content = yaml.load(f_n, Loader=yaml.FullLoader)

print(f_n_content, f_n_content == data_yaml)
