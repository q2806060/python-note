from multiprocessing import Value, Process, Lock

def makemoney(money, lock):
    for i in range(1000):
        lock.acquire()
        money.value += 1
        lock.release()

def usemoney(money, lock):
    for i in range(1000):
        lock.acquire()
        money.value -= 1
        lock.release()

if __name__ == '__main__':
    money = Value('i', 5000)
    lock = Lock()
    p1 = Process(target=makemoney, args=(money,lock))
    p2 = Process(target=usemoney, args=(money,lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(money.value)


















