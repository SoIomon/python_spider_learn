# -*- coding:utf-8 -*-

import requests
import json

'''#HTTP六种基本请求类型
r = requests.get("http://httpbin.org/post")
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")'''

#r = requests.head("http://httpbin.org/get")
#print r.headers

'''payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
print r.url
print r.headers'''

'''payload = {'key1': 'value1', 'key2': 'value2'}   #利用data参数，传入基本参数
r = requests.post("http://httpbin.org/post", data=payload)
print r.text'''

'''url = 'http://httpbin.org/post'  #postJSON数据格式
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))    #运用json.dumps()方法把表单数据格式序列化
print r.text'''

'''url = 'http://httpbin.org/post'     #上传文件
files = {'file': open('a.txt', 'rb')}
r = requests.post(url, files=files)
print r.text'''

'''r = requests.get('http://httpbin.org/get')
print r.status_code
print r.status_code == requests.codes.ok
bad_r = requests.get('http://httpbin.org/status/404')
#print bad_r.status_code
print bad_r.raise_for_status()'''

'''headers = {
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
}
headers['Content-Type']     #访问相应头字段
print headers.get('content-type')'''

'''url = 'http://httpbin.org/cookies'  #发送cookies到服务器
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text'''

'''r = requests.get('http://github.com', allow_redirects=False)    #重定向参数allow_redirects，默认True
print r.url     #在github中默认重定向至https://github.com
print r.history'''

#requests.get('http://github.com', timeout=0.001)    #设置超时 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应

'''s = requests.Session()      #建立一个长久的会话。
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')     #设置cookies
r = s.get("http://httpbin.org/cookies")     #获取cookies
print(r.text)'''

#s = requests.Session()
#s.headers.update({'x-test': 'true'})        #第一次上传x-test
#r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})       #第二次上传
#print r.text
'''运行结果如下,两个参数都传送，若同名，则后来的会覆盖前一次上传的值
    {
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.13.0",
    "X-Test": "true",
    "X-Test2": "true"
  }
}'''
#r = s.get('http://httpbin.org/headers', headers={'x-test': None})   #运用None ，去除全局变量中某个变量
#print r.text
'''{
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.13.0"
  }
}'''

