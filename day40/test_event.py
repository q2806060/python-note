from threading import Event



e = Event()

e.set()

print(e.is_set())

e.clear()

print(e.is_set())

e.wait(timeout=2)

print('**********End***********')




























