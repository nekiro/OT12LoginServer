import mysql.connector
from mysql.connector import Error as MySqlError

class Database:
    def __init__(self):
        self.cn = None

    def open(self):
        try:
            self.cn = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="8.0")
            return True
        except MySqlError as err:
            print(err)
            return False
    
    def __del__(self):
        if self.cn:
            self.cn.close()

    def execute_query(self, query):
        try:
            cursor = self.cn.cursor()
            cursor.execute(query)
            cursor.close()
        except MySqlError as err:
            print(err)
    
    def store_query(self, query):
        try:
            cursor = self.cn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except MySqlError as err:
            print(err)

    def escape_string(self, str):
        return "'" + str + "'"
