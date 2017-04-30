# -*- coding:utf-8 -*-

import urllib2
import re

#爬取糗事百科类
class QSBK:

    #初始化方法
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        #初始化爬取页码,默认第一次爬取第 1 页
        self.nowPageNo = 1
        #段子存储队列
        self.ContentQueue = []

    #获取页面原码方法
    def getPage(self,pageNo):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageNo)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e, "reason"):
                print u"链接糗事百科失败，错误原因",e.reason
                return None

    #处理页面信息(标题，内容，页码)方法
    def getInfo(self):
        pageCode = self.getPage(self.nowPageNo)
        if not pageCode:
            print u'页面加载失败'
            return None
        pattern = re.compile('<h2>(.*?)</h2.*?<span>(.*?)</.*?number">(.*?)</',re.S)
        items = re.findall(pattern, pageCode)
        # 用来储存每页的段子的列表
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(), item[1].strip(), item[2].strip()])
        return pageStories

    #展示页面信息
    def showInfo(self):
        pageInfo = self.getInfo()
        if pageInfo:
            for item in pageInfo:
                print u"第%d页\t发布人:%s\t\t赞:%s\n%s" % (self.nowPageNo, item[0], item[2], item[1])

    #运行程序
    def start(self):
        self.showInfo()


test = QSBK()
test.start()