import logging
import pathlib

# Порт поумолчанию для сетевого ваимодействия
DEFAULT_PORT = 7777
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
ENCODING = 'utf-8'

# Прококол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
RESPONSE_DEFAULT_IP_ADDRESS = 'response_default_ip_address'

"""
Журналирование (логгирование) с использованием модуля logging
Расширенная настройка. Форматирование, обработчики
"""
# назначаем папку для хранения log files
logs = (pathlib.Path.home() / 'Desktop' / 'Клиент-серверные приложения на Python'
        / 'Client-server-applications-in-Python.git' / 'Lesson_5' / 'homework' /
        'log' / 'log_files')

# Создать логгер - регистратор верхнего уроовня
# с именем basic
LOG = logging.getLogger('basic')

# файл, в который добавляются журналируемые сообщения
CRIT_HAND = logging.FileHandler(f'{logs}\\app.log', encoding='utf-8')

# Создать объект Formatter
# Определить формат сообщений
FORMATTER = logging.Formatter("%(name)s %(levelno)s %(levelname)s %(pathname)s "
                              "%(filename)s %(funcName)s %(module)s %(lineno)d "
                              "%(created)f %(asctime)s %(msecs)s %(thread)d "
                              "%(threadName)s %(process)d %(message)s")

# подключить объект Formatter к обработчику
CRIT_HAND.setFormatter(FORMATTER)

# Добавить обработчик к регистратору
LOG.addHandler(CRIT_HAND)
LOG.setLevel(logging.DEBUG)

# LOG.debug('Отладочная информация')
# LOG.info('Информационное сообщение')
# LOG.warning('Предупреждение')
# LOG.critical('Критическое общение')
