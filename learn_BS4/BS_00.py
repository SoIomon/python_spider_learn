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
'''for string in soup.strings:
    print(repr(string))
for string in soup.stripped_strings:
    print (repr(string))'''

'''父节点
.parent 属性'''
'''p = soup.p
print p.parent.name
content = soup.head.title.string
print content.parent.name'''

'''兄弟节点
知识点：.next_sibling  .previous_sibling 属性
兄弟节点可以理解为和本节点处在统一级的节点，.next_sibling 属性获取了该节点的下一个兄弟节点，
.previous_sibling 则与之相反，如果节点不存在，则返回 None
注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，
因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行'''
#print soup.p.next_sibling
#print soup.p.prev_sibling
#print soup.p.next_sibling.next_sibling

'''全部兄弟节点
.next_siblings  .previous_siblings 属性
通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出'''
#for sibling in soup.a.next_siblings:
#    print (repr(sibling))

'''前后节点
.next_element  .previous_element 属性
与 .next_sibling  .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次
比如 head 节点为'''
#print soup.head.next_element

'''所有前后节点
知识点：.next_elements  .previous_elements 属性
通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,
就好像文档正在被解析一样
'''
#for element in last_a_tag.next_elements:
 #   print (repr(element))

'''搜索文档树
（1）find_all( name , attrs , recursive , text , **kwargs )
find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
1）name 参数
name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
A.传字符串
最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,
下面的例子用于查找文档中所有的<b>标签'''
print soup.find_all('b')