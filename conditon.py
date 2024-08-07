from threading import *
from time import sleep

con = Condition()

# how condition works is like

# T1 -> Lock() -> check cond == True -> wait() -> Block()
# thread mutex    done var                      

done = 1 

def task(name):
    global done
    with con:
        if done == 1:
            done = 2
            print('Before wait()',name)
            con.wait()
            print('After wait()', name)

        else:
            for i in range(5):
                print('*',end='')
                sleep(1)
            print()
            print('Signaling condition varibale cond', name)
            con.notify_all()
            print('Notification done',name)

if __name__ == '__main__':

    t1 = Thread(target=task, args=('A',))
    t2 = Thread(target=task, args=('B',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

