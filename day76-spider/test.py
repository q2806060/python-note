import requests,os 
from agents import *
import pymongo

# resp = requests.get("http://tieba.baidu.com/p/5979753599?pn=10", headers=headers)
# print(resp.url)

# path = os.path.dirname(__file__)
# print(path)

# //div[@class="pb_content clearfix"]//div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src
# //div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src


conn = pymongo.MongoClient("127.0.0.1", 27017)
db = conn["qiushidb"]
myset = db["duanzi"]
duanzis = myset.find()
for duanzi in duanzis:

    print(duanzi)