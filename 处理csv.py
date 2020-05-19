# -*- coding:utf-8 -*-
'''
@Author: fhj
@Blog: https://i.csdn.net/#/uc/profile
@E-mail: 2655398311@qq.com
@File: 处理csv.py
@CreateTime:2020/5/8 10:16
'''


import pandas as pd

def read_csv(path):
    r'C:\Users\hjfan\Desktop\bozhu1_blog.csv'
    data = pd.read_csv(path)
    total_data = pd.DataFrame()
    order_id_list = list(set(data['platform_cid'].values.tolist()))

    for ind,order_id in enumerate(order_id_list):
        tmp_data = data[data.platform_cid == order_id]
        tmp_data.to_csv(r"C:\Users\hjfan\Desktop\{}.csv".format(str(ind)))

# read_csv(path=r'C:\Users\hjfan\Desktop\bozhu1_blog.csv')

'''
标签处理工具
'''