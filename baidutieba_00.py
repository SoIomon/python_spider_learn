# -*- coding:utf-8 -*-

import urllib2
import re

#百度贴吧爬虫类
class BDTB:

    #初始化方法，传入基地址，是否只看楼主
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)

    #传入页码，获取帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read()
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"链接百度贴吧失败，错误原因",e.reason
                return None

    #获取页面标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>',re.S)
        result = pattern.search(page)
        if result:
            #print result.group(1)
            return result.group(1).strip()
        else:
            return None

    #获取帖子页面数
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num".*?</span>.*?<span.*?>(.*?)</span>')
        result = pattern.search(page)
        if result:
            print  result.group(1)
            return result.group(1).strip()
        else:
            return None

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
#bdtb.getPage(1)
#bdtb.getTitle()
bdtb.getPageNum()