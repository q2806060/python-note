from multiprocessing import Manager, Pool 

def write():
    for s in ['a','b','c']:
        q.put(s)

def read():
    while True:
        try:
            print(q.get(block=False))
        except:
            break

if __name__ == '__main__':
    q = Manager().Queue()
    pool = Pool()
    pool.apply(func=write)
    pool.apply(func=read)
    pool.close()
    pool.join()
































