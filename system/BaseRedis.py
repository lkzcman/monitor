import redis
from system.singleton import singleton
from system.config import conf


@singleton
class Connect(object):
    redis = object()

    def __init__(self):
        redis_config = conf.conf["redis"]
        redis_conn = redis.ConnectionPool(host=redis_config["host"], port=redis_config["port"],
                                          db=redis_config["db"], password=redis_config["password"])
        self.redis = redis.Redis(connection_pool=redis_conn)


class BaseRedis(object):
    redis = object()

    def __init__(self):
        conn = Connect()

        self.redis = conn.redis
        self.prefix = conf.conf["redis"]["prefix"]


base_redis = BaseRedis()
