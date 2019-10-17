from multiprocessing import Pool, Manager 

def f1(n, q):
    for i in range(1, n+1):
        q.put((2, i))

def f2(n, q):
    for i in range(n):
        m, n = q.get()
        print(m ** n )

if __name__ == '__main__':
    q = Manager().Queue()
    pool = Pool()
    pool.apply(func=f1, args=(10,q))
    pool.apply(func=f2, args=(10,q))
    pool.close()
    pool.join()











