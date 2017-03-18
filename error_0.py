import urllib2

requese = urllib2.Request("http://www.xxxx.com")
try:
    urllib2.urlopen(requese)
except urllib2.URLError, e:
    print e.reason