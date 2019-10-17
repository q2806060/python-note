import tensorflow as tf 
import numpy as np 


def fun01():
    # 定义一个二维数组
    # 使用tf.constant方法定义一个二维常量m2
    # 将m1装换为张量类型
    # 对m1和m2进行加运算
    # 输出运算的结果
    m1 = np.array([[1, 2],[3, 4]])
    m2 = tf.constant([[1, 2],[3, 4]], dtype=tf.float32)
    m3 = tf.convert_to_tensor(m1, dtype=tf.float32)
    m4 = m2 + m3
    # # 创建会话
    # sess = tf.Session()
    # # 执行m4，并返回执行的结果
    # res = sess.run(m4)
    # print(res) 
    # sess.close()
    with tf.Session() as sess:
        res = sess.run(m4)
        print(res)
        
fun01()
# m = tf.Variable([[1, 2], [3, 4]], dtype=tf.float32)
