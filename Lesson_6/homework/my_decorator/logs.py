import logging

# Инициализация клиентского логера
CLIENT_LOGGER = logging.getLogger('client')
DECORATOR_LOG = logging.getLogger('decorator')
SERVER_LOGGER = logging.getLogger('server')


def log():
    """Внешняя функция (формально - декоратор)."""

    def decorator(func):
        """Сам декоратор."""

        def decorated(*args, **kwargs):
            """Обертка."""
            res = func(*args, **kwargs)
            DECORATOR_LOG.debug(f'обращение к декорируемой функции {func.__name__}')
            DECORATOR_LOG.debug(f'Функция {func.__name__}, аргументы {args}{kwargs}.')
            if func.__name__ == 'create_presence':
                CLIENT_LOGGER.debug(f"Сформировано {'PRESENCE'}"
                                    f" сообщение для пользователя {res['user']['account_name']}")
            elif func.__name__ == 'process_client_message':
                SERVER_LOGGER.debug(f'Разбор сообщения от клиента : {res}')
            return res

        return decorated

    return decorator
