#!/usr/bin/env python
'''api main entrance'''
import web
import re
import urllib2

urls = (
  '/rss/tyxz.xml', "clean_tyxz",
)

class clean_tyxz:
    def GET(self):
        url = 'http://donatino.skygate.cn/rss/rss20/21/'
        f = urllib2.urlopen(url)
        info = f.info()
        xml = f.read()
        f.close()
        web.header('Content-Type', 'text/xml;charset=utf-8')
        return self.clean(xml)

    def clean(self, xml):
        def repl_func(match):
            return chr(int(match.group(1), 16))
        return re.sub('&#x([a-f0-9]+);', repl_func, xml)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
