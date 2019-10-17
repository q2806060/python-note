from multiprocessing import Process, Array

def f1(shareData):
    for i in shareData:
        print(i)

    shareData[0] = 1000

if __name__ == '__main__':
    shareData = Array('i', [1, 2, 3, 4, 5])
    p = Process(target=f1, args=(shareData,))
    p.start()
    p.join()

    for i in shareData:
        print(i)










