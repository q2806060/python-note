import pymysql
import warnings

# 创建连接
db = pymysql.connect("101.132.141.19", "root", "123456", charset="utf8")
# 创建游标
cursor = db.cursor()

# 忽略警告
warnings.filterwarnings("ignore")

cdb = "create database if not exists maoyandb"
cursor.execute(cdb)

db.commit()
print("save ok.")
cursor.close()
db.close()