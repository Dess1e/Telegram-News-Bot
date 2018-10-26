#!/usr/bin/python3
from TelegramSession import TelegramSession

import logging
logging.basicConfig(format='[%(asctime)s] - %(levelname)s - %(message)s', level=logging.INFO)

TELEGRAM_TOKEN = open('token').read()

if __name__ == '__main__':
    s = TelegramSession(TELEGRAM_TOKEN)
    s.main_loop()

