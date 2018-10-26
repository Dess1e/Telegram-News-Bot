#!/usr/bin/python3
import sqlite3


class SQLiteDB:
    DB_NAME = 'users.db'

    def __init__(self):
        self.conn = None
        try:
            open(SQLiteDB.DB_NAME, 'r').close()
        except FileNotFoundError:
            self._create_db()
        self.connect()

    @staticmethod
    def _create_db():
        conn = sqlite3.connect(SQLiteDB.DB_NAME)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE Users(telegram_id int, modules varchar)
        ''')
        conn.commit()
        conn.close()

    def get_user(self, tg_id):
        c = self.conn.cursor()
        c.execute('''
            SELECT modules FROM Users WHERE telegram_id=?
        ''', (tg_id,))
        f = c.fetchall()
        if f:
            return f[0][0]
        else:
            return None

    def get_all_users(self):
        c = self.conn.cursor()
        c.execute('''
            SELECT * FROM Users
        ''')
        f = c.fetchall()
        if f:
            return f

    def add_user(self, tg_id, modules: str):
        c = self.conn.cursor()
        c.execute('''
            INSERT INTO Users(telegram_id, modules) VALUES(?, ?) 
        ''', (tg_id, modules))
        self.conn.commit()

    def rm_user(self, tg_id):
        c = self.conn.cursor()
        c.execute('''
            DELETE FROM Users WHERE telegram_id=?
        ''', (tg_id,))
        self.conn.commit()

    def update_user(self, tg_id, new_modules: str):
        c = self.conn.cursor()
        c.execute('''
            UPDATE Users SET modules=? WHERE telegram_id=?
        ''', (new_modules, tg_id))
        self.conn.commit()

    def connect(self):
        self.conn = sqlite3.connect(SQLiteDB.DB_NAME, check_same_thread=False)

