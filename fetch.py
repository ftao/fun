#!/usr/bin/env python
import urllib2
import re

def clean(xml):
    def repl_func(match):
        return chr(int(match.group(1), 16))
    return re.sub('&#x([a-f0-9]+);', repl_func, xml)


def fetch_and_cache(url):
    xml = urllib2.urlopen(url).read()
    cleaned_xml = clean(xml)

    cache_file = open('static/rss/tyxz.xml', 'w')
    cache_file.write(cleaned_xml)
    cache_file.close()

    return cleaned_xml


if __name__ == "__main__":
    url = 'http://donatino.skygate.cn/rss/rss20/21/'
    fetch_and_cache(url)
    print 'Fetch and Cache OK'
