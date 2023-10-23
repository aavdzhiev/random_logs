import logging
from rand_sentence import random_sentence
from time import sleep

logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('log-app.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)


def main():
    while True:
        logger.debug(random_sentence())
        logger.info(random_sentence())
        logger.warning(random_sentence())
        logger.error(random_sentence())
        logger.critical(random_sentence())
        sleep(10)


if __name__ == '__main__':
    main()