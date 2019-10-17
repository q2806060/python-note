import hmmlearn.hmm as hl
import os 
import numpy as np 
import scipy.io.wavfile as wf 
import python_speech_features as sf 


def search_files(directory):
    directory = os.path.normpath(directory)

    # {'apple':[dir, dir, dir], 'banana':[dir..]}
    objects = {}
    # 当前目录，当前目录子目录，文件列表
    for curdir, subdirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                label = curdir.split(os.path.sep)[-1]
                if label not in objects:
                    objects[label] = []
                path = os.path.join(curdir, file)
                objects[label].append(path)
    return objects

train_samples = search_files('C:\\Users\\Administrator\\Desktop\\sucai\\ml_data\\speeches\\training')


# 整理训练集，把每一个类别中的音频的mfcc摞在一起，基于隐马模型开始训练
train_x, train_y = [], []
for label, filenames in train_samples.items():
    mfccs = np.array([])
    for filename in filenames:
        sample_rate, sigs = wf.read(filename)
        mfcc = sf.mfcc(sigs, sample_rate)
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            mfccs = np.append(mfccs, mfcc, axis=0)
    train_x.append(mfccs)
    train_y.append(label)

# 基于隐马模型进行训练，把所有类别的模型都存起来
models = {}
for mfccs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(n_components=4, covariance_type='diag', n_iter=1000)
    models[label] = model.fit(mfccs)

# 读取测试集中的文件，使用每个模型对文件进行评分，取分支大的模型对应的label作为
test_samples = search_files('C:\\Users\\Administrator\\Desktop\\sucai\\ml_data\\speeches\\testing')

# 整理测试集，把每一个类别中的音频的mfcc摞在一起
test_x, test_y = [], []
for label, filenames in test_samples.items():
    mfccs = np.array([])
    for filename in filenames:
        sample_rate, sigs = wf.read(filename)
        mfcc = sf.mfcc(sigs, sample_rate)
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            mfccs = np.append(mfccs, mfcc, axis=0)
    test_x.append(mfccs)
    test_y.append(label)

# 使用7个模型，对每一个文件进行预测得分
pred_test_y = [] 
# test_x一共7个样本，遍历7次，每次验证1个文件
for mfccs in test_x:
    best_score, best_label = None, None
    for label, model in models.items():
        score = model.score(mfccs)
        if (best_score is None) or (best_score<score):
            best_score, best_label = score, label
    pred_test_y.append(best_label)

print(test_y)
print(pred_test_y)
        