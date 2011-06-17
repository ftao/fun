#!/usr/bin/env python
import urllib2
import os
import re
import redis
import settings

redis_conn = redis.Redis(host=settings.redis_host, port=settings.redis_port, db=settings.redis_db)

def clean(xml):
    def repl_func(match):
        return chr(int(match.group(1), 16))
    return re.sub('&#x([a-f0-9]+);', repl_func, xml)


def fetch_and_cache(url):
    xml = urllib2.urlopen(url).read()
    cleaned_xml = clean(xml)

    save_cache('rss/tyxz.xml', cleaned_xml)

    return cleaned_xml


'''
CACHE_DIR = os.path.join(os.path.dirname(__file__), 'static')
def save_cache(path, value):
    cache_file = open(os.path.join(CACHE_DIR, 'rss/tyxz.xml'), 'w')
    cache_file.write(value)
    cache_file.close()

def load_cache(path):
    return open(os.path.join(CACHE_DIR, 'rss/tyxz.xml'), 'r').read()

'''

def save_cache(path, value):
    redis_conn.set(path, value)

def load_cache(path):
    return redis_conn.get(path)

if __name__ == "__main__":
    import os 
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    url = 'http://donatino.skygate.cn/rss/rss20/21/'
    fetch_and_cache(url)
    print 'Fetch and Cache OK'


