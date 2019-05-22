# file name : dbModule.py
# pwd : /tripWithU/app/module/dbModule.py

import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='mypassword',
                                  db='tripwithu',
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def excute(self, query, args={}):
        self.cursor.execute(query,args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit():
        self.db.commit()


