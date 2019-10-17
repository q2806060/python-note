from threading import Thread
import time 

def f1(name, scends):
    print('%s process start.' %name)
    time.sleep(scends)
    print('%s process end, spend time %d scends.' %(name, scends))

if __name__ == '__main__':
    lst = []

    for i in range(3):
        t = Thread(target=f1, args=(i+1, 2))
        lst.append(t)
        t.start()

    for m in lst:
        m.join()































