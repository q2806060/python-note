from threading import Thread, Event
import time


s = None


def python():
    global s 
    s = 'I like Python.'
    e.set()


if __name__ == '__main__':
    e = Event()
    t = Thread(target=python)
    t.start()
    print('Fa said:Python too bad.')
    e.wait()
    if s == 'I like Python.':
        print('Welcome come.')
    else:
        print('Next class wait you.')
    t.join()






























