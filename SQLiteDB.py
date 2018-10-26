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
        c.execute('''CREATE TABLE Users(
                                    telegram_id int,
                                    state int,
                                    modules varchar)''')
        conn.commit()
        conn.close()

    def connect(self):
        self.conn = sqlite3.connect(SQLiteDB.DB_NAME, check_same_thread=False)


if __name__ == '__main__':
    b = SQLiteDB()
    print(b.get_token(228))
