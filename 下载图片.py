import os
import pandas as pd
import time
# os.makedirs('D:/image/', exist_ok=True)
from sqlalchemy import create_engine
import tqdm
import requests
user ='fanhaojie'
passwd ='Chenfan@123'
host ='10.228.86.203'
port ='11101'
dbname1 = 'test'
engine2 = create_engine("mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8"%(user,passwd,host,port,dbname1))

# sql = 'select * from test.image_4'
# IMAGE_URL = pd.read_sql(sql,engine2)

# IMAGE_URL = pd.read_csv(r'C:\Users\hjfan\Desktop\zhiyi_img_url.csv',encoding='ISO-8859-1')
IMAGE_URL = pd.read_csv(r'C:\Users\hjfan\Desktop\all_images.csv',encoding='gbk')
import time
aa = IMAGE_URL.to_dict('reocrd')
ac = []
for i in aa:
    # .strip('.0')
    try:
        start_time = time.time()
        a = i['images_url_05']
        b = str(i['taobao_goods_id'])
        import requests
        r = requests.get('http:' + a)
        print(r)
        #+b+'_'+str(count)+
        path = "D://all_goods_info_images/"+b+'.jpg'
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
    except:
        print("下载失败++++++++++++++",i['taobao_goods_id'])
        shibai = i['taobao_goods_id']
        aaa = {"shibai":shibai,"image_5":i['images_url_05']}
        ac.append(aaa)
shibaiwrite = pd.DataFrame(ac)
shibaiwrite.to_excel('shibai.xlsx')
end_time = time.time()
print(end_time - start_time)
        # with open('aa.txt','wb') as f:
        #     ac = str(i['b.item_id']).encode()
        #     f.write(ac)
        #     f.write('\n').encode()


