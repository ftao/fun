#coding=utf-8

redis_host = 'localhost'
redis_port = 6379
redis_db = 0


try:
    from local_settings import *
except ImportError,e:
    pass
