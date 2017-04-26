# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import thread
import time

#糗事百科爬虫类
class QSBK:

    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否运行的变量
        self.enable = False

    #传入某一页的索引得页面代码
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #构建请求的request
            request = urllib2.Request(url, headers= self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            #将页面转化为utf-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"链接糗事百科失败，错误原因",e.reason
                return None

    #传入某一页代码，返回本页不带图片的段子列表
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败。。。"
            return None
        pattern = re.compile('<h2>(.*?)</h2.*?content">.*?<span>(.*?)</.*?number">(.*?)</',re.S)
        items = re.findall(pattern, pageCode)
        #用来储存每页的段子
        pageStories = []
        #遍历正则匹配信息
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
        return pageStories

    #加载并提取页面内容，加到列表中
    def loadPage(self):
        #如果当前未读页面少于2，则新加载一页
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    #调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self,pageStories,page):
        #遍历一遍段子
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t\t赞:%s\n%s" %(page,story[0],story[2],story[1])

    #开始方法
    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()