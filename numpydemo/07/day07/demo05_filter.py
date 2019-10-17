"""
demo05_filter.py
"""
import numpy as np
import matplotlib.pyplot as mp
import scipy.io.wavfile as wf
import numpy.fft as nf

# 读取音频文件, 获取音频的基本信息: 
# 采样个数/采样周期/每个采样点的声音值.  
# 绘制音频的时域: 时间/位移图像.
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

# 基于傅里叶变换, 获取音频频域信息, 
# 绘制频域: 频率/能量图像.
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

# 将低频噪声去除后绘制音频频域: 频率/能量图像.
fund_freq = freqs[noised_pows.argmax()]
# 找到所有噪声的下标
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

# 基于逆向傅里叶变换,生成时域的音频信号, 
# 绘制时域: 时间/位移图像.
filter_sigs = nf.ifft(filter_ffts)
mp.subplot(2,2,3)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
mp.plot(times[:178], filter_sigs[:178], 
	c='dodgerblue', label='Filter Sigs')
mp.legend()

# 重新生成音频文件
wf.write('../da_data/filter.wav', sample_rate,
	filter_sigs.astype(np.int16))

mp.tight_layout()
mp.show()
