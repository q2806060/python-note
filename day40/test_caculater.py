from multiprocessing import Process 
from threading import Thread
import time


def CPU(x, y):
    z = 0
    while z < 7000000:
        x += 1
        y += 1
        z += 1


def write():
    with open('test.txt', 'w') as f:
        for i in range(150000):
            f.write('Hello world.\n')


def read():
    with open('test.txt', 'r') as f:
        lines = f.readlines()


def IO():
    write()
    read()

#******************************************************

# if __name__ == '__main__':
#     begin = time.time()
#     ts = []
#     for i in range(10):
#         t = Thread(target=CPU, args=(1,1))
#         ts.append(t)
#         t.start()

#     for i in ts:
#         i.join()

#     end = time.time()

#     print('Spend time:%.2f' %(end-begin))

#*********************************************************

# if __name__ == '__main__':
#     begin = time.time()
#     ps = []
#     for i in range(10):
#         p = Process(target=CPU, args=(1,1))
#         ps.append(p)
#         p.start()

#     for i in ps:
#         i.join()

#     end = time.time()

#     print('Spend time:%.2f' %(end-begin))

#*************************************************************

# if __name__ == '__main__':
#     begin = time.time()
#     ts = []
#     for i in range(10):
#         t = Thread(target=IO)
#         ts.append(t)
#         t.start()

#     for i in ts:
#         i.join()

#     end = time.time()

#     print('Spend time:%.2f' %(end-begin))

#*************************************************************

if __name__ == '__main__':
    begin = time.time()
    ps = []
    for i in range(10):
        p = Process(target=IO)
        ps.append(p)
        p.start()

    for i in ps:
        i.join()

    end = time.time()

    print('Spend time:%.2f' %(end-begin))


















