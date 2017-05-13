# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

'''Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。
Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。'''

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')

#print soup.prettify()

#Tag
'''print soup.title
print soup.head
print soup.a
print soup.p'''

'''对于 Tag，它有两个重要的属性，是 name 和 attrs，soup 对象本身比较特殊，它的 name
即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。'''
'''print soup.name
print soup.head.name
print soup.p.attrs'''

#NavigableString
'''print soup.p.string
print type(soup.p.string)'''

#BeautifulSoup
'''BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，
是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性来感受一下'''
'''print type(soup.name)
print soup.name
print soup.attrs'''

#Comment
'''Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注
释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。'''
'''print soup.a
print soup.a.string
print type(soup.a.string)'''

#遍历文档树

#tag 的 .content 属性可以将tag的子节点以列表的方式输出
#print soup.head.contents
#print soup.head.contents[0]

#.children它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。
#print soup.head.children    #生成了一个list生成器对象
#for child in soup.body.children:
#    print child

'''.descendants
.contents 和 .children 属性仅包含tag的直接子节点，.descendants
 属性可以对所有tag的子孙节点进行递归循环，和 children类似，我们也需要遍历获取其中的内容。'''
#for child in soup.descendants:
#    print child

'''.string
如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。
如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容.'''
#print soup.head.string
#print soup.head.string
#print type(soup.body)

'''.strings
获取多个内容，不过需要遍历获取。
.stripped_strings
输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容.
'''
for string in soup.strings:
    print(repr(string))
for string in soup.stripped_strings:
    print (repr(string))

