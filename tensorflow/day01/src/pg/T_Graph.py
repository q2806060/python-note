import tensorflow as tf 
from src.pg.DataUtil import *
import numpy as np 
'''
构建训练模型:LeNet5
对数据进行训练
并对训练的结果进行性能评估
'''
# 输入层，输出层
imput_x = tf.placeholder(dtype=tf.float32, shape=[None, 784])
imput_img = tf.reshape(input_x, shape=[-1, 28, 28, 1])
output_y = tf.placeholder(dtype=tf.float32, shape=[None, 10])
output_cls = tf.argmax(output_y, dimension=1)

# 卷积层1
'''
32个5*5大小的卷积核
卷积运算：same
激活函数：relu
输出：32个28*28
'''
conv1 = tf.layers.conv2d(inputs=input_img,      # 输入数据
                        filters=32,             # 卷积核的数量
                        kernel_size=[5,5],      # 卷积核的大小
                        padding='same',         # 卷积运算的方式
                        activation=tf.nn.relu)  # 激活函数

# 池化层1
'''
池化核：2*2最大值池化
输出：32个14*14
'''
pool1 = tf.layers.max_pooling2d(inputs=conv1, 
                                pool_size=[2, 2],
                                strides=2)



# 测试
with tf.Session() as ress:
    ress.run(tf.global_variables_initializer())
    c1, p1 = ress.run([conv1, pool1], feed_dict={input_x:mnist.train.images[:2]})
    print(c1)

'''
构建训练模型：定义超参数
神经网络的层数
每一层神经元的数量
神经元之间的连接方式
每层使用的激活函数

训练参数：
权重参数和阈值
'''