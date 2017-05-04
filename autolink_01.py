#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import time
import os

#自动连接校园网类
class AutoLink:

    #初始化方法,传入用户名和密码
    def __init__(self, username, password):
        #校园网登录url
        self.url = 'http://192.168.168.168/0.htm'
        self.username = username
        self.password = password

    #自动连接方法
    def link(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
            }
            data = {
                'DDDDD': self.username,
                'upass': self.password,
                '0MKKey': '(unable to decode value)',
                'v6ip': ''
            }
            post_data = urllib.urlencode(data)
            request = urllib2.Request(self.url, post_data, headers)
            response = urllib2.urlopen(request)
            code = response.read().decode('GB2312')
            pattern = re.compile('<title>(.*?)</title>',re.S)
            result = re.findall(pattern, code)
            print result[0]
        except urllib2.URLError,e:
            if hasattr(e, "reason"):
                print u"连接失败，错误原因",e.reason
                return None

    # 判断网络连通性
    def judegConnect(self):
        exit_code = os.system('ping www.baidu.com')
        #exit_code 连通时为0 否则为1
        return exit_code

if __name__ == '__main__':
    id = raw_input(u'请输入账号：')
    password = raw_input(u'请输入密码：')
    a = AutoLink(id,password)
    a.link()
    while True:
        time.sleep(30)
        if (a.judegConnect()):
            a.link()
