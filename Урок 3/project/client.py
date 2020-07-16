from socket import SOCK_STREAM, socket


'''
Функции клиента:
сформировать presence-сообщение;
отправить сообщение серверу;
получить ответ сервера;
разобрать сообщение сервера;
параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера;
port — tcp-порт на сервере, по умолчанию 7777.
'''


def json_to_b(action):
    with open(f'{action}.json') as f_n:
        f_n_content = f_n.read()
        return f_n_content.encode('utf-8')


sock = socket(type=SOCK_STREAM)
msg = json_to_b('authenticate')  # quit, presence,msg
sock.connect(('127.0.0.1', 8888))
sock.send(msg)
data = sock.recv(1024)
sock.close()
data = data.decode('utf-8')
data = eval(data)
if data['response'] == 200:
    print(data['alert'])
