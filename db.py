import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="087907210769323928Ti@",
            database="etab_db"
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params, fetch_lastrowid=False):
        self.cursor.execute(query, params)
        self.conn.commit()
        if fetch_lastrowid:
            return self.cursor.lastrowid

    def get_lastrowid(self):
        return self.cursor.lastrowid

    def fetch_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
