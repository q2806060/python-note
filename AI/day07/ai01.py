import scipy.io.wavfile as wf 
import python_speech_features as sf 
import matplotlib.pyplot as mp 

sample_rate, sigs = wf.read('C:\\Users\\Administrator\\Desktop\\sucai\\ml_data\\speeches\\training\\apple\\apple01.wav')
mfcc = sf.mfcc(sigs, sample_rate)
print(mfcc.shape)

mp.matshow(mfcc.T, cmap='gist_rainbow')
mp.title('MFCC')
mp.xlabel('Samples', fontsize=14)
mp.ylabel('Features', fontsize=14)
mp.tick_params(labelsize=10)
mp.show()