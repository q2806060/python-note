from threading import Lock, Thread


m = 0
n = 0

def f1():
    while True:
        with lock:
            if m != n:
                print('m =', m, 'n =', n)

if __name__ == '__main__':
    lock = Lock()
    t = Thread(target=f1)
    t.start()
    while True:
        with lock:
            m += 1
            n += 1

    t.join()






























