import mysql.connector
from mysql.connector import Error as MySqlError
import models

class Database:
    def __init__(self):
        self.cn = None

    def open(self):
        try:
            conf = models.config["database"]
            self.cn = mysql.connector.connect(host=conf.get("host", "127.0.0.1"), user=conf.get("user", "root"), password=conf.get("password", ""), database=conf.get("name", ""), port=conf.get("port", 3306))
            self.cn.autocommit = True
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
        return "'{}'".format(str)
