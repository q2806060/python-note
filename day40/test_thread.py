from threading import Thread
import os
import time
import pygame

n = 1

def music():
    
    for i in range(2):
        time.sleep(2)
        print('Play the blooming life.', os.getpid())
    global n 
    n = 1000
    print(n)

if __name__ =='__main__':
    t = Thread(target=music)
    t.start()
    t.join()

    for i in range(2):
        time.sleep(3)
        print('Play the cat sound.', os.getpid())
    
    pygame.mixer.init()
    pygame.mixer.music.load('day40/qest.mp3')
    pygame.mixer.music.play()
    time.sleep(60)
    print('The main process: n =', n)





























