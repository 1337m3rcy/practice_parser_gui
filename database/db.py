import sqlite3


class Database:
    def __init__(self, db_name='db.db'):
        self.db_name = db_name

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Измененная структура таблицы с добавленными столбцами Protocol, Country, Region, City и Anonymity
        cursor.execute('''CREATE TABLE IF NOT EXISTS proxies
                          (id INTEGER PRIMARY KEY,
                           ip TEXT,
                           port INTEGER,
                           protocol TEXT,
                           country TEXT,
                           region TEXT,
                           city TEXT,
                           anonymity TEXT)''')

        conn.commit()
        conn.close()

    def save_proxies(self, proxies):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        for proxy in proxies:
            cursor.execute("INSERT INTO proxies (ip, port, protocol, country, region, city, anonymity) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (proxy['ip'], proxy['port'], proxy['protocol'], proxy['country'], proxy['region'], proxy['city'], proxy['anonymity']))

        conn.commit()
        conn.close()

    def get_proxies(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT ip, port, protocol, country, region, city, anonymity FROM proxies")
        proxies = cursor.fetchall()

        conn.close()

        return proxies
