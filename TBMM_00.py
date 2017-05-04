# -*- coding:utf-8 -*-

import urllib2
import re


# 爬取https://mm.taobao.com/json/request_top_list.htm中的模特信息类
class TBMM:

    #初始化方法
    def __init__(self):
        self.baseURL = 'https://mm.taobao.com/json/request_top_list.htm'

    def getPage(self,Index):
        url = self.baseURL + '?page=' + str(Index)
        request = urllib2.Request(url)
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
            info = 'https://mm.taobao.com/self/model_info.htm?user_id='+ str(item[0]) +'&is_coment=false'   #详细信息页面url
            contents.append([info ,item[1], item[2], item[3], item[4]])
        return contents

    '''def saveImg(self,imageURL,fileName):
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
            return False'''

a = TBMM()
a.getConnent(1)