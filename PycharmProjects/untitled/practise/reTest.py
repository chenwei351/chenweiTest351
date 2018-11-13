# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#coding:utf-8

import requests


r=requests.post(
    url='http://m.cyw.com/index.php?m=api&c=cookie&a=setcity',
    data={'cityId':434})
print (r.json())