import pymysql
from system.singleton import singleton
from system.config import conf


@singleton
class Connect(object):
    db = object()

    def __init__(self):
        self.db_config = conf.conf["db"]
        self._db()

    def _db(self):
        self.db = pymysql.connect(self.db_config["host"], self.db_config["user"], self.db_config["password"],
                                  self.db_config["db_name"], use_unicode=self.db_config["use_unicode"],
                                  charset=self.db_config["charset"])

    def ping(self):
        self.db.ping(reconnect=True)


class BaseModule(object):
    update_data = list()
    db = object()
    cursor = object()

    def __init__(self):
        self.conn = Connect()
        self.db = self.conn.db
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def base_insert(self, sql, data):
        self.cursor.executemany(sql, data)
        self.db.commit()

    def fetchone(self, sql, args=None):
        self.conn.ping()
        self.cursor.execute(sql, args)
        data = self.cursor.fetchone()
        return data

    def fetchall(self, sql, args=None):
        self.conn.ping()
        self.cursor.execute(sql, args)
        data = self.cursor.fetchall()
        return data
