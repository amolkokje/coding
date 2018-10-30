# 18.1 --> digit manipulation

# 18.2: Write a method to shuffle a deck of cards. It must be a perfect shuffle: in other words, each of the 52! permutations of the deck has to be equally likely. Assume that you are given a random number generator which is perfect.

import random
def shuffle(deck):
    n = len(deck)
    for i in range(n):
        r = i
        while r == i:  # to ensure the position of card changes
            r = random.randint(0, n-1)
            deck[i], deck[r] = deck[r], deck[i]
        
# 18.3: Write a method to randomly generate a set of m integers from an array of size n. Each element must have equal probability of being chosen.
# NOTE: different solution in the book, same as deck shuffle
        
def choose(arr, m):        
    chosen = dict()
    n = len(arr)
    for _ in range(m):
        done = False
        while not done:
            r = random.randint(0, n-1)  # to ensure I dont choose the same again
            if not chosen.get(r):
                chosen[r] = arr[r]
                done = True
    return chosen.values()
        

# 18.4:  Write a method to count the number of 2s between 0 and
# brute force with memoization. Book has number manipulation method, which is not very self-explanatory

def memoize(func):
    class memodict(dict):
        def __missing__(self, key):
            self[key] = func(key)
            return self[key]
            
    return memodict().__getitem__        

def count_twos(x):
    return len(filter(lambda y:y=='2', [ch for ch in str(x)] ) )  
    
@memoize    
def count_twos_in_range(num):
    if num == 2:
        return 1
    else:
        return count_twos(num) + count_twos_in_range(num-1)
    
        
        
    
if __name__ == '__main__':

    print '---------------------------------------------------'
    deck = range(52)
    shuffle(deck)
    print 'shuffled deck = {}'.format(deck)
    
    print '---------------------------------------------------'
    arr = range(10)
    m = 4
    print 'arr={}, m={}, chosen={}'.format(arr, m, choose(arr, m))
    
    print '---------------------------------------------------'
    arr = [ 4, 10, 12, 22, 222 ]
    for a in arr:
        print 'a={}, count_2 in range={}'.format(a, count_twos_in_range(a)) 