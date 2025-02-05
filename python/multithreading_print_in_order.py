# ref: https://leetcode.com/problems/print-in-order/editorial/?envType=problem-list-v2&envId=concurrency

from concurrent.futures import ThreadPoolExecutor
from threading import Lock


# 12345
class PrintNumbersEvenOdd:

    def __init__(self, n):
        self.n = n

        self.evenlock = Lock()
        self.oddlock = Lock()

        self.evenlock.acquire() # since will print even first
    
    def print_even(self):
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.evenlock.acquire()
                print(i)
                self.oddlock.release()

    def print_odd(self):
        for i in range(1, self.n + 1):
            if i % 2 != 0:
                self.oddlock.acquire()
                print(i)
                self.evenlock.release()







# 0102030405
class PrintNumbersZeroEvenOdd:

    def __init__(self, n):
        self.n = n

        self.zerolock = Lock()
        self.evenlock = Lock()
        self.oddlock = Lock()

        # since will print zero first   
        self.oddlock.acquire()
        self.evenlock.acquire() 

    def print_zero(self):
        for i in range(1, self.n + 1):
            self.zerolock.acquire()
            print(0)
            if i % 2 == 0:
                self.evenlock.release()
            else:
                self.oddlock.release()
    
    def print_even(self):
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.evenlock.acquire()
                print(i)
                self.zerolock.release()

    def print_odd(self):
        for i in range(1, self.n + 1):
            if i % 2 != 0:
                self.oddlock.acquire()
                print(i)
                self.zerolock.release()


# from threading import Thread
# threadslist = []
# print_numbers = PrintNumbersEvenOdd(10)

# # start odd thread first, then even thread
# threadslist.append(Thread(target=print_numbers.print_odd))
# threadslist.append(Thread(target=print_numbers.print_even))
# for t in threadslist:
#     t.start()

# # wait for all threads to finish
# for t in threadslist:
#     t.join()


# ------------

from threading import Thread
threadslist = []
print_numbers = PrintNumbersZeroEvenOdd(10)

# start zero thread first, then odd thread, then even thread
threadslist.append(Thread(target=print_numbers.print_zero))
threadslist.append(Thread(target=print_numbers.print_odd))
threadslist.append(Thread(target=print_numbers.print_even))
for t in threadslist:
    t.start()

# wait for all threads to finish
for t in threadslist:
    t.join()
