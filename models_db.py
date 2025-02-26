import sqlite3


class Db:
    def __init__(self, db_name):
        self.db_name = db_name



    def connect(self):
        self.conn=sqlite3.connect(self.db_name)
        self.cursor=self.conn.cursor()



    def creat_table(self, name):
        self.name = name
        self.connect()
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name}(
                            user_id INTEGER PRIMARY KEY,
                            username TEXT)''')
        self.conn.commit()
        self.close()


    def insert_user(self, user_id: int, username: str):
        self.connect()
        self.cursor.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
        self.conn.commit()
        self.close()

    def close(self):
        self.conn.close()

