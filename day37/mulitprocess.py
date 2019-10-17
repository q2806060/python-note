from multiprocessing import Process

print('Fa process do samething.')
def fun1():
    print('Son process do fun1.')

p = Process(target=fun1)
if __name__ == '__main__':
    p.start()


























