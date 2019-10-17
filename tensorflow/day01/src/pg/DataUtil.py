'''
导入库
'''
from tensorflow.examples.tutorials.mnist import input_data 
import matplotlib.pyplot as mp 
import numpy as np 
import tensorflow as tf 

'''
数据加载
'''



# 代码测试
mnist = loadData('../../dataset/mnist/')



'''
数据可视化
'''

def plotData(imgs, cls, pred=None):
    assert len(imgs) == len(cls) == 9
    f, subs = mp.subplots(3,3)
    lbl = '' # x轴标题
    for i, sub in enumerate(subs.flat):
        sub.imshow(imgs[i].reshape(28, 28), cmap='binary')
        if pred is None:
            lbl = 'true:{0}'.format(cls[i])
        else:
            lbl = 'true:{0};pred:{1}'.format(cls[i], pred[i])
    mp.show()

plotData(mnist.train.images[:9], mnist.train.cls[:9])