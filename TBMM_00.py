# -*- coding:utf-8 -*-

import urllib2
import urllib
import tool
import re


# 爬取https://mm.taobao.com/json/request_top_list.htm中的模特信息类
class TBMM:

    #初始化方法
    def __init__(self):
        self.baseURL = 'https://mm.taobao.com/json/request_top_list.htm'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def getPage(self,Index):
        url = self.baseURL + '?page=' + str(Index)
        request = urllib2.Request(url,headers=self.headers)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    def getConnent(self,Index):
        page = self.getPage(Index)
        pattern = re.compile('pic-word.*?<a href="//mm.taobao.com/(.*?).htm"'   #id号
                             '.*?<img src="(.*?)"'  #头像
                             '.*?<a class="lady-name.*?>(.*?)</a>'  #姓名
                             '.*?<strong>(.*?)</strong>'    #年龄
                             '.*?<span>(.*?)</span>'    #地址
                             ,re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            info = 'https://mm.taobao.com/self/model_info.htm?user_id=96614110&is_coment=false'   #详细信息页面url
            contents.append([info ,item[1], item[2], item[3], item[4]])
        #print contents
        return contents

    # 获取MM个人详情页面
    def getDetailPage(self, infoURL):
        request = urllib2.Request(infoURL,headers=self.headers)
        response = urllib2.urlopen(request)
        page = response.read().decode('gbk')
        print page
        pattern = re.compile('<div .*?"mm-p-info mm-p-domain-info">.*?<h4>',re.S)
        item = re.findall(pattern,page)
        print item
        return page

    '''# 获取个人文字简介
    def getBrief(self, page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
        result = re.search(pattern, page)
        return self.tool.replace(result.group(1))

    # 获取页面所有图片
    def getAllImg(self, page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
        # 个人信息页面所有代码
        content = re.search(pattern, page)
        # 从代码中提取图片
        patternImg = re.compile('<img.*?src="(.*?)"', re.S)
        images = re.findall(patternImg, content.group(1))
        return images

    # 保存多张写真图片
    def saveImgs(self, images, name):
        number = 1
        print u"发现", name, u"共有", len(images), u"张照片"
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = name + "/" + str(number) + "." + fTail
            self.saveImg(imageURL, fileName)
            number += 1

    # 保存头像
    def saveIcon(self, iconURL, name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon." + fTail
        self.saveImg(iconURL, fileName)

    # 保存个人简介
    def saveBrief(self, content, name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName, "w+")
        print u"正在偷偷保存她的个人信息为", fileName
        f.write(content.encode('utf-8'))

    # 传入图片地址，文件名，保存单张图片
    def saveImg(self, imageURL, fileName):
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print u"正在悄悄保存她的一张图片为", fileName
        f.close()

    def saveImg(self,imageURL,fileName):
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        f.close()

    def saveBrief(self, content, name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName, "w+")
        print u"正在偷偷保存她的个人信息为", fileName
        f.write(content.encode('utf-8'))

    # 创建新目录
    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

            # 传入起止页码，获取MM图片
            # 将一页淘宝MM的信息保存起来

            # 将一页淘宝MM的信息保存起来

    def savePageInfo(self, pageIndex):
        # 获取第一页淘宝MM列表
        contents = self.getContents(pageIndex)
        for item in contents:
            # item[0]个人详情URL,item[1]头像URL,item[2]姓名,item[3]年龄,item[4]居住地
            print u"发现一位模特,名字叫", item[2], u"芳龄", item[3], u",她在", item[4]
            print u"正在偷偷地保存", item[2], "的信息"
            print u"又意外地发现她的个人地址是", item[0]
            # 个人详情页面的URL
            detailURL = item[0]
            # 得到个人详情页面代码
            detailPage = self.getDetailPage(detailURL)
            # 获取个人简介
            brief = self.getBrief(detailPage)
            # 获取所有图片列表
            images = self.getAllImg(detailPage)
            self.mkdir(item[2])
            # 保存个人简介
            self.saveBrief(brief, item[2])
            # 保存头像
            self.saveIcon(item[1], item[2])
            # 保存图片
            # self.saveImgs(images, item[2])

    def savePagesInfo(self, start, end):
            for i in range(start, end + 1):
                print u"正在偷偷寻找第", i, u"个地方，看看MM们在不在"
                self.savePageInfo(i)
    '''

a = TBMM()
a.getConnent(1)
a.getDetailPage('https://mm.taobao.com/self/model_info.htm?user_id=96614110&is_coment=false')