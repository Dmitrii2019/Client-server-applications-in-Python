import logging

from homework.common.settings import CRIT_HAND, LOG

# Определить формат сообщений лога, если прописаный в settings не подходит
formatter_client = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")

CRIT_HAND.setFormatter(formatter_client)

# Добавить обработчик к регистратору
LOG.addHandler(CRIT_HAND)

# назначаем уровень важности, если прописаный в settings не подходит(DEBUG)
# LOG.setLevel(logging.INFO)

# LOG.debug('Отладочная информация')
