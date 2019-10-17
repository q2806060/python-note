# 数据分析DAY07

### 特征值与特征向量

对于n阶方阵A, 如果存在数a和非零n维列向量x, 使得Ax=ax, 则称a是矩阵A的一个特征值, x是矩阵A属于特征值的特征向量.

```python
# 提取方阵A的特征值与特征向量
# eigvals: 一组特征值
# eigvecs: 特征值对应的特征向量
eigvals, eigvecs = np.linalg.eig(A)
# 通过特征值与特征向量 逆向推导原方阵
S = eigvecs * np.diag(eigvals) * eigvecs.I
```

案例:

```python
"""
demo01_eig.py 特征值与特征向量
"""
import numpy as np

A = np.mat('1 5 8; 2 5 7; 8 2 4')
# 提取特征值与特征向量
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)
# 逆向推导原方阵
S = np.mat(eigvecs) * \
	np.mat(np.diag(eigvals)) * \
	np.mat(eigvecs).I
print(S)
eigvals[1:] = 0
S = np.mat(eigvecs) * \
	np.mat(np.diag(eigvals)) * \
	np.mat(eigvecs).I
print(S)
```

案例: 读取图片的亮度矩阵, 提取特征值与特征向量, 保留部分特征值, 重新生成新的亮度矩阵, 绘制图片.

```python
"""
demo02_eig.py 提取图片的特征值
"""
import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as mp

image = sm.imread('../da_data/lily.jpg', True)
print(type(image), image.shape)

# 提取image矩阵的特征值与特征向量
eigvals, eigvecs = np.linalg.eig(image)
# 抹掉一部分特征值 重新生成新的图片
print(eigvals.shape)
eigvals[130:] = 0
S = np.mat(eigvecs) * \
	np.mat(np.diag(eigvals)) * \
	np.mat(eigvecs).I
S = S.real
mp.figure('Lily Features',facecolor='lightgray')
mp.subplot(1,2,1)
mp.xticks([])
mp.yticks([])
mp.imshow(image, cmap='gray')
mp.subplot(1,2,2)
mp.xticks([])
mp.yticks([])
mp.imshow(S, cmap='gray')
mp.tight_layout()
mp.show()
```

### 奇异值分解

有一个矩阵M, 可以分解为3个矩阵U S V, 使得UxSxV等于M. U与V都是正交矩阵(乘以自身的转置矩阵结果为单位矩阵). 那么S矩阵主对角线上的元素称为矩阵M的奇异值, 其他元素都为0.

```python
# 奇异值分解  U与V都是正交矩阵
# s: 奇异值数组
U, s, V = np.linalg.svd(M)
# 逆向推导原矩阵:
S = U * np.diag(s) * V
```

案例: 读取图片亮度矩阵,提取奇异值.保留部分奇异值,重新生成图片.

```python
# 奇异值分解 
U, s, V = np.linalg.svd(image)
S2 = np.mat(U)*np.mat(np.diag(s))*np.mat(V)
# 保留部分奇异值  生成图片
s[100:] = 0
S3 = np.mat(U)*np.mat(np.diag(s))*np.mat(V)

mp.subplot(2,2,3)
mp.xticks([])
mp.yticks([])
mp.imshow(S2, cmap='gray')
mp.subplot(2,2,4)
mp.xticks([])
mp.yticks([])
mp.imshow(S3, cmap='gray')
```

### 快速傅里叶变换(fft)

**什么是傅里叶变换?**

傅里叶定理: 任何一条周期曲线, 无论多么跳跃或不规则, 都能表示成一组光滑正弦曲线叠加之和. 傅里叶变换即是把这条周期曲线拆解成一组光滑正弦曲线的过程.

傅里叶变换的目的是将时域(时间域)上的信号转变为频域(频率域)上的信号, 随着域的不同,对同一个事物的了解角度也随之改变. 因此在时域中某些不好处理的地方, 放在频域中就可以较为简单的处理. 这样可以大量减少处理的数据量.

傅里叶定理:
$$
y = A_1sin(\omega_1x+\phi_1) + 
A_2sin(\omega_2x+\phi_2) + .. +C
$$
快速傅里叶变换相关API:

```python
import numpy.fft as nf
# 通过采样数与采样周期,得到fft分解所得曲线的频率数组
# 采样周期: x轴相邻两点的距离
freqs = nf.fftfreq(采样数量, 采样周期)

# 通过原函数值序列, 经过fft后, 得到复数数组
# 复数数组的长度即是拆解出正弦函数的个数
# 复数数组每个元素的模,代表每个正弦曲线的振幅
# 复数数组每个元素的辅角,代表每个正弦曲线的相位角
复数序列 = nf.fft(原函数值序列)

# 逆向傅里叶变换
原函数值序列 = nf.ifft(复数序列)
```

案例: 基于傅里叶变换, 拆解方波.

```python
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
```

**基于傅里叶变换的频域滤波**

含噪信号是高能信号与低能噪声叠加的信号, 可以通过傅里叶变换的频域滤波实现简单降噪.

通过FFT使含噪信号转换为含噪频谱, 手动取出低能噪声, 留下高能频谱后,再通过IFFT生成高能信号. 

1. 读取音频文件, 获取音频的基本信息: 采样个数/采样周期/每个采样点的声音值.  绘制音频的时域: 时间/位移图像.

```python
sample_rate, noised_sigs = \
	wf.read('../da_data/noised.wav')
print(noised_sigs.shape) 
times = np.arange(len(noised_sigs))/sample_rate

mp.figure('Filter', facecolor='lightgray')
mp.subplot(2,2,1)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
mp.plot(times[:178], noised_sigs[:178], 
	c='dodgerblue', label='Noised Sigs')
mp.legend()
mp.show()

```

2. 基于傅里叶变换, 获取音频频域信息, 绘制频域: 频率/能量图像.

```python
freqs = nf.fftfreq(times.size, 1/sample_rate)
noised_ffts = nf.fft(noised_sigs)
noised_pows = np.abs(noised_ffts)
mp.subplot(222)
mp.title('Frequency Domain', fontsize=16)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=8)
mp.grid(linestyle=":")
mp.semilogy(freqs[freqs>0], noised_pows[freqs>0],
	c='orangered', label='Noised')
mp.legend()
```

3. 将低频噪声去除后绘制音频频域: 频率/能量图像.

```python
noised_inds = np.where(freqs != fund_freq)
filter_ffts = noised_ffts.copy()
filter_ffts[noised_inds] = 0
filter_pows = np.abs(filter_ffts)
mp.subplot(224)
mp.title('Frequency Domain', fontsize=16)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=8)
mp.grid(linestyle=":")
mp.plot(freqs[freqs>0], filter_pows[freqs>0],
	c='orangered', label='Filter')
mp.legend()
```

4. 基于逆向傅里叶变换,生成时域的音频信号, 绘制时域: 时间/位移图像.

```python
filter_sigs = nf.ifft(filter_ffts)
mp.subplot(2,2,3)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
mp.plot(times[:178], filter_sigs[:178], 
	c='dodgerblue', label='Filter Sigs')
mp.legend()
```

5. 生成音频文件

```python
wf.write('../da_data/filter.wav', sample_rate, filter_sigs.astype(np.int16))
```

### 随机数模块

生成服从特定统计规律的随机数序列.

#### 二项分布(binomial)

二项分布是重复n次独立试验的伯努利试验.  每次试验只有两种可能的结果, 而且两种结果发生与否相互独立相互对立. 事件发生与否的概率在每一次独立试验中都保持不变.

```python
# 产生size个随机数, 每个随机数来自n次尝试中的成功
# 的次数, 其中每次尝试成功的概率为p
# 这样产生的随机数即符合二项分布规律.
np.random.binomial(n, p, size)
```

案例: 某人投篮命中率0.3, 投10次, 进5个的概率.

```python
# 某人投篮命中率0.3, 投10次, 进5个的概率.
r = np.random.binomial(10, 0.3, 100000)
p = (r==5).sum() / r.size
print(p)
```

#### 超几何分布

```python
# 产生size个随机数, 每个随机数为在总样本中随机抽取
# nsample个样本后,好样本的个数.
# 总样本由ngood个好样本和nbad个坏样本组成.
np.random.hypergeometric(
    ngood, nbad, nsample, size)
```

案例: 7个好苹果, 3个坏苹果, 抽出3个苹果, 求抽出2个好苹果的概率.

```python
# 7个好苹果, 3个坏苹果, 抽出3个苹果, 
# 求抽出2个好苹果的概率
r = np.random.hypergeometric(7, 3, 3, 100000)
p = (r==2).sum() / r.size
print(p)
```

#### 正态分布(normal)

```python
# 产生符合标准正态分布的size个随机数
# 期望=0, 标准差=1
np.random.normal(size)
# 产生符合正态分布的size个随机数
# 期望=1, 标准差=10
np.random.normal(loc=1, scale=10, size)
```

### 杂项功能

#### 排序

```python
np.msort(array)
```

**联合间接排序**

```python
# 先按照主序列排序,若值相同,则按照参考序列排序.
indices = np.lexsort((参考序列, 主序列))
```

案例: 为商品排序.   价格  ->  销量

```python
# 为商品排序.   价格  ->  销量
p = np.array(['Apple','HuaWei','OPPO','MI','VIVO'])
prices = [8888, 4500, 3999, 2999, 3999]
totals = np.array([100, 200, 99, 110, 80])

indices = np.lexsort((totals*-1, prices))
print(p[indices])
```

**为复数数组排序**

```python
# 按照实部排序, 对于实部相同的复数则按照虚部排序
# 直接返回结果数组.
np.sort_complex(复数数组)
```

**插入排序**

若有需求要向有序数组中插入元素, 使数组依然有序, numpy提供了searchsorted方法查询并返回可插入位置数组.

```python
indices = np.searchsorted(有序序列, 待插入序列)
np.insert(原数组, 位置序列, 待插入序列)
```

```python
a = np.array([1, 2, 4, 6, 8])
b = np.array([3, 5])
indices = np.searchsorted(a, b)
print(indices)
a = np.insert(a, indices, b)
print(a)
```

#### 插值

scipy提供了常见的插值算法, 可以通过样本数据的一定的规律生成插值器函数. 若我们给出函数的自变量, 将会得到函数值. 插值器可以通过一组离散的样本数据得到一个连续的函数, 从而可以计算样本中不包含的自变量所对应的函数值.

```python
import scipy.interpolate as si
si.interp1d(
	离散点的水平坐标,
    离散点的垂直坐标,
    kind='linear'  #插值算法 默认:linear线性插值
)
```

案例:

```python
"""
demo08_interpolate.py 插值器
"""
import numpy as np
import matplotlib.pyplot as mp
import scipy.interpolate as si

min_x = -50
max_x = 50
dis_x = np.linspace(min_x, max_x, 15)
dis_y = np.sinc(dis_x)
mp.figure('interpolate',facecolor='lightgray')
mp.title('Interpolate',fontsize=16)
mp.grid(linestyle=':')
mp.scatter(dis_x, dis_y, marker='D', 
	c='red', label='Points')

# 通过这组散点, 构建线性插值器函数
linear = si.interp1d(dis_x, dis_y)
lin_x = np.linspace(min_x, max_x, 1000)
lin_y = linear(lin_x)
mp.plot(lin_x, lin_y, c='dodgerblue', 
		label='Linear Interpolate')

# 构建三次样条插值器
cubic = si.interp1d(dis_x, dis_y, kind='cubic')
cub_y = cubic(lin_x)
mp.plot(lin_x, cub_y, c='orangered', 
		label='Cubic Interpolate')

mp.legend()
mp.show()
```

#### 积分

```python
import scipy.integrate as si

def f(x):
    return 2*x**2 + 3*x +4
# f: 函数名
# -5: 积分下限
# 5: 积分上限
# area: 定积分的结果
area = si.quad(f, -5, 5)[0]
```

#### 简单图像处理

scipy.ndimage提供了一些简单的图像处理.如:高斯模糊, 图像旋转, 边缘识别等功能.













