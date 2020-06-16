import subprocess

import chardet

# 1. Каждое из слов «разработка», «сокет», «декоратор» представить
# в строковом формате и проверить тип и содержание соответствующих
# переменных. Затем с помощью онлайн-конвертера преобразовать
# строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'
words = [word_1, word_2, word_3]

for word in words:
    print(f'тип = {type(word)}, соержимое = {word}')

word_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word_2 = '\u0441\u043e\u043a\u0435\u0442'
word_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
words = [word_1, word_2, word_3]

for word in words:
    print(f'тип = {type(word)}, соержимое = {word}')

# 2. Каждое из слов «class», «function», «method» записать в байтовом
# типе без преобразования в последовательность кодов
# (не используя методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

word_1 = b'class'
word_2 = b'function'
word_3 = b'method'
words = [word_1, word_2, word_3]

for word in words:
    print(f'тип = {type(word)}, соержимое = {word} , длина = {len(word)}')

# 3. Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе.

# 'attribute', 'type' - можно записать в байтовом виде, так как буквы латинские
# 'класс', 'функция' - нельзя записать в байтовом виде, так как буквы кириллицы

# 4. Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование
# (используя методы encode и decode).

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'
words = [word_1, word_2, word_3, word_4]

for word in words:
    word = str.encode(word, encoding='utf-8')
    print(f'байтовое представление = {word}')
    print(f'строковое представление = {bytes.decode(word, encoding="utf-8")}')

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
# результаты из байтовового в строковый тип на кириллице.

args = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in YA_PING.stdout:
    result = chardet.detect(line)
    data = line.decode(result['encoding']).encode('utf-8')
    print(data.decode('utf-8'))

args = ['ping', 'youtube.com']
YA_PING = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in YA_PING.stdout:
    result = chardet.detect(line)
    data = line.decode(result['encoding']).encode('utf-8')
    print(data.decode('utf-8'))

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

with open('test_file.txt', 'w') as f_n:
    f_n.write('«сетевое программирование», «сокет», «декоратор»')
    print(f'кодировка по умолчанию {f_n.encoding}')

with open('test_file.txt', 'r', encoding='cp1251') as f_n:
    for el_str in f_n:
        print(el_str, end='')
