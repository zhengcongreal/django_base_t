from django.test import TestCase

# Create your tests here.
from redis import *

if __name__ == "__main__":
    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = StrictRedis()
        # 添加键name，值为itheima
        # result=sr.hset("user","name","zhengcong")
        # print(sr.hgetall("user"))
        # sr.hdel("user","name")
        # sr.delete('user')
        result = sr.keys()
        print(result)
    except Exception as e:
        print(e)
