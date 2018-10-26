from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler

from SQLiteDB import SQLiteDB
from Exceptions import SessionException
from TelegramUser import TelegramUser

from time import sleep
import logging
import pdb


class TelegramSession:
    def __init__(self, tg_token):
        self.users = {}
        self.upd = Updater(tg_token)
        self.dp = self.upd.dispatcher
        self.users_db = SQLiteDB()

        self.fetch_db()
        self.init_logic()

    def add_user(self, tg_id):
        if tg_id in self.users:
            raise SessionException
        else:
            self.users[tg_id] = TelegramUser(id=tg_id)

    def get_user(self, tg_id):
        usr = self.users.get(tg_id)
        if usr:
            return usr
        else:
            raise SessionException

    def init_logic(self):
        dp = self.dp
        dp.add_handler(CommandHandler('start', self.cmd_start))
        dp.add_handler(CommandHandler('debug', self.cmd_debug))
        dp.add_handler(CommandHandler('stop', self.cmd_stop))
        dp.add_handler(CommandHandler('menu', self.cmd_menu))

        u = self.upd
        j = u.job_queue
        j.run_repeating(self.job_scrape, interval=60, first=0)

    def fetch_db(self):
        ...

    def cmd_start(self, bot, update):
        """Should be blocking because writes to db"""

        usr = update.message.from_user
        ...

    def cmd_debug(self, bot, update):
        update.message.reply_text('dropped to pdb session, bye')
        pdb.set_trace()

    def cmd_menu(self, bot, update):
        usr = update.message.from_user

        def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
            menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
            if header_buttons:
                menu.insert(0, header_buttons)
            if footer_buttons:
                menu.append(footer_buttons)
            return menu

        button_list = [
            InlineKeyboardButton('Switch Mode', callback_data='switch_mode'),
            InlineKeyboardButton('jora', callback_data='1'),
            InlineKeyboardButton('jora', callback_data='2'),
            InlineKeyboardButton('jora', callback_data='3')
        ]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
        update.message.reply_text('boba', reply_markup=reply_markup)

    def cmd_stop(self, bot, update):
        ...

    def job_scrape(self, bot, job):
        ...

    def main_loop(self):
        self.upd.start_polling()
