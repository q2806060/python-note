from multiprocessing import Process 
import time

name = 'Zhiruo Zhou'

def f1():
    print('Son process name = %s' %name)

p = Process(target=f1)


time.sleep(1)

print('Fa process name = %s' %name)

if __name__ == '__main__':
    p.start()












































