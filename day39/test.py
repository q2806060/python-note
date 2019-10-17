from multiprocessing import Pipe,Process,Queue

def write():
    for i in range(10):
        if q.full():
            print('List full.')
            break
        q.put(i)

def read():

    while True:
        try:
            print(q.get(block=True, timeout=1))
        except:
            print('List empty.')
            break
    
q = Queue(4)

if __name__ == '__main__':
    
    p1 = Process(target=write)
    p2 = Process(target=read)
    p1.start()
    p2.start()
    p1.join()
    p2.join()






































