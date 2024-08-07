from threading import *
import time

lock = Lock()
count = 0

def task(process):

    lock.acquire()

    global count

    for i in range(10**2):
        temp = count
        time.sleep(0.0000001)
        count = temp+1
        
    lock.release()


if __name__ == '__main__':
    t2 = Thread(target=task, args=('A',))
    t1 = Thread(target=task, args=('B',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(count)
