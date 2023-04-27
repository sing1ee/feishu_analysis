import os
import redis

queue_key = "__queue__"

__poll = redis.ConnectionPool(host='chat-redis', db=0, password=os.getenv('REDIS_PWD'), port=6379)
__rclient = redis.Redis(connection_pool=__poll)

print('redis init ', __rclient.get('__version__'))


def push_msg(msg):
    __rclient.lpush(queue_key, msg)

