#!/usr/bin/env python
'''api main entrance'''
import web
import re
from fetch import fetch_and_cache
import urllib2

urls = (
  '/rss/tyxz.xml', "clean_tyxz",
)

class clean_tyxz:
    def GET(self):
        web.header('Content-Type', 'text/xml;charset=utf-8')

        url = 'http://donatino.skygate.cn/rss/rss20/21/'
        cleaned_xml = fetch_and_cache(url)

        return cleaned_xml

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
