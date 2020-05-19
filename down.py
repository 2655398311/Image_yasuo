import requests
import os
import re
a = ['https://img.alicdn.com/imgextra/i1/57220545/O1CN011FteIoCkqhDm2S1_!!57220545.jpg',
     'http://img.alicdn.com/imgextra/i3/57220545/TB29LVMmp9gSKJjSspbXXbeNXXa_!!572205451.jpg']
for i in a:
    try:
        print('第一次请求')
        aa = re.sub('https:|http:','',i)
        b = requests.get('http:'+aa)
        aaa = b.status_code
        if aaa==404:
            print(i)
    except:
        pass
# bb = re.sub('https:|http:', '', i)


    # print(aa)