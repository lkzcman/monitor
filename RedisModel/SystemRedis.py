from system.BaseRedis import BaseRedis
import json
import time


class SystemRedis(BaseRedis):
    def __init__(self):
        BaseRedis.__init__(self)

    def add(self, data):
        print data
        result = self.redis.zadd("system_monitor", json.dumps(data), int(time.time()))
        return result

system_redis = SystemRedis()
