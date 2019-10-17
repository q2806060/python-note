from multiprocessing import Semaphore, Process 
import time
import os

def f1(sem):
    print('%d want to do process.' %os.getpid())
    sem.acquire()
    print('%d take it.' %os.getpid())
    time.sleep(1)
    sem.release()

if __name__ == '__main__':

    sem = Semaphore(3)

    pList = []
    for i in range(10):
        p = Process(target=f1, args=(sem,))
        pList.append(p)
        p.start()

    for p in pList:
        p.join()


















