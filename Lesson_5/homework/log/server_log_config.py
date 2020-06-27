import logging
from logging import handlers

from homework.common.settings import CRIT_HAND, ENCODING, LOG

# Определить формат сообщений лога, если прописаный в settings не подходит
formatter_server = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")

CRIT_HAND.setFormatter(formatter_server)

# Добавить обработчик к регистратору
LOG.addHandler(CRIT_HAND)

# назначаем уровень важности, если прописаный в settings не подходит(DEBUG)
# LOG.setLevel(logging.INFO)

# LOG.debug('Отладочная информация')

handlers.TimedRotatingFileHandler('app.log', when='D', interval=1,
                                  backupCount=0, encoding=ENCODING, delay=False, utc=False)
