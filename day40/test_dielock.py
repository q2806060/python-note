from threading import Thread, Lock 
import time

lock1 = Lock()
lock2 = Lock()

def func1():
    lock1.acquire()
    print('Process 1 lock lock1.')
    time.sleep(0.1)
    while True:
        result = lock2.acquire(timeout=1)
        if result:
            print('Process 1 lock lock2.')
            print('Hi, process 1.')
            
            lock2.release()
            break
        else:
            lock1.release()

def func2():
    lock2.acquire()
    print('Process 2 lock lock2.')
    time.sleep(0.1)
    lock1.acquire()
    print('Process 2 lock lock1.')
    print('Hi, process 2.')
    lock1.release()
    lock2.release()


if __name__ =='__main__':
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()






























