# _*_ coding:utf-8 -*-

import re

pattern = re.compile(r'hello')

resule1 = re.match(pattern, 'hello')
resule2 = re.match(pattern, 'helloo QD')
resule3 = re.match(pattern, 'helo QD')
resule4 = re.match(pattern, 'hello QD')

if resule1:
    print resule1.group()
else:
    print '1F'

if resule2:
    print  resule2.group()
else:
    print  '2F'

if resule3:
    print resule3.group()
else:
    print '3F'

if resule4:
    print resule4.group()
else:
    print '4F'