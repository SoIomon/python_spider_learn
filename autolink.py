# -*- coding -*-

import urllib2
import urllib

url = 'http://192.168.168.168/0.htm'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
'''headers = {
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests':'keep-alive',
'User-Agent':user_agent ,
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Referer': 'http://192.168.168.168/0.htm',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language': 'zh-CN,zh;q=0.8'}'''
headers ={
'User-Agent':user_agent
}
data = {
'username':'101001972000800',
'password':'252838'
}
request = urllib2.Request(url,data=urllib.urlencode(data),headers=headers)
response = urllib2.urlopen(request)
print response.read()