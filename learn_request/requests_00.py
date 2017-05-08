# -*- coding:utf-8 -*-

import requests
from PIL import Image
from io import BytesIO

r = requests.get('http://gtd.alicdn.com/sns_logo/i2/TB1XZ1PQVXXXXaJXpXXSutbFXXX_120x120.jpg')
i = Image.open(BytesIO(r.content))
print i