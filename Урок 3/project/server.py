import json
from socket import SOCK_STREAM, socket


'''
Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания
(по умолчанию слушает все доступные адреса).
'''


def json_to_b(action):
    with open(f'{action}_server.json', encoding='utf-8') as f_n:
        f_n_content = f_n.read()
        print(eval(f_n_content)['alert'])
        return f_n_content.encode('utf-8')


sock = socket(type=SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(1)
conn, addr = sock.accept()

print(f'Соединение установлено: {addr}')


try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.decode('utf-8')
        jsonData = json.loads(data)
        if jsonData['action'] == 'quit':
            conn.send(json_to_b(jsonData['action']))
            conn.close()
            break

        conn.send(json_to_b(jsonData['action']))
finally:
    conn.close()
