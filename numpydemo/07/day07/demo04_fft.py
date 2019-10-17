"""
demo04_fft.py  傅里叶变换
"""
import numpy as np
import matplotlib.pyplot as mp
import numpy.fft as nf

x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# 叠加1000条曲线
y = np.zeros(x.size)
for i in range(1, 1000):
	y += 4/(2*i-1)*np.pi * np.sin((2*i-1)*x)

# 对y做傅里叶变换, 绘制频域图像
ffts = nf.fft(y)
# 获取傅里叶变换的频率序列
freqs = nf.fftfreq(x.size, x[1]-x[0])
pows = np.abs(ffts)

mp.figure('FFT', facecolor='lightgray')
mp.subplot(121)
mp.grid(linestyle=':')
mp.plot(x, y,linewidth=2)
mp.subplot(122)
mp.grid(linestyle=':')
mp.plot(freqs[freqs>0], pows[freqs>0], 
	    c='orangered')
# 通过复数数组,经过ifft操作, 得到原函数
y2 = nf.ifft(ffts)
mp.subplot(121)
mp.plot(x, y2, linewidth=7, alpha=0.5)

mp.show()

