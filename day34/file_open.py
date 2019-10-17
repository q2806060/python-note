from pymongo import MongoClient
import bson.binary

from_img = 'test.jpg'
to_img = 'test_new.jpg'

def save_img(myset):
    with open(from_img, 'rb') as f:
        data = f.read()
        content = bson.binary.Binary(data)
        myset.insert({
            'filename':from_img,
            'data':content,
        })
    print('save ok')
    return

def get_img(myset):
    img = myset.find_one({'filename':from_img})
    with open(to_img, 'wb') as f:
        f.write(img['data'])
    print('save new file ok.')
    return


conn = MongoClient('localhost', 27017)
db = conn.gridfs    #获取库对象
myset = db.image        #获取集合对象

#save_img(myset)         #调用存文件函数
get_img(myset)

conn.close()




































