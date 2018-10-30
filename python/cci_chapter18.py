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
    
    
# 18.5: You have a large text file containing words. Given any two words, find the shortest distance (in terms of number of words) between them in the file. If the operation will be repeated many times for the same file (but different pairs of words), can you optimize your solution?   

# if you have to search distance multiple times, then store all locations for each word in a dict, and then iterate over the values for keys word-1 and word-2 to see which have min difference
# if do not need to search multiple times, then use approach below

def find_min_distance(book, word1, word2):
    last_position_word1 = -1
    last_position_word2 = -1
    
    n = len(book)
    min_distance = 99999
    for i in range(n):
        found_word = False
        
        if book[i] == word1:
            last_position_word1 = i
            found_word = True
        
        elif book[i] == word2:
            last_position_word2 = i
            found_word = True
        
        if found_word and (last_position_word1 != -1) and (last_position_word2 != -1):
            diff = abs(last_position_word1 - last_position_word2)
            if diff < min_distance:
                min_distance = diff
                    
    return min_distance            
            
    
        
# 18.6: Describe an algorithm to find the smallest one million numbers in one billion numbers. Assume that the computer memory can hold all one billion numbers
# Book's fastest solution is selection rank algorithm, a special quik-sort case. Python: http://www.ardendertat.com/2011/10/27/programming-interview-questions-10-kth-largest-element-in-array/ -> SDE

import heapq
def find_smallest(arr, m):
    arr_heap = []
    for i in range(len(arr)):
        heapq.heappush(arr_heap, arr[i])
    
    smallest = []
    for _ in range(m):
        smallest.append(heapq.heappop(arr_heap))
    return smallest
    
    
# 18.7: Given a list of words, write a program to find the longest word made of other two words in the list

def find_longest(words):
    
    n = len(words)
    
    def sort_by_length(wlist):        
        def greater_than(w1, w2):
            return True if len(w1) >= len(w2) else False        
        
        # fastest is merge sort, using bubble sort here for simplicity        
        for _ in range(n):
            for i in range(n-1):
                # descending order of length
                if greater_than(wlist[i+1], wlist[i]):
                    wlist[i], wlist[i+1] = wlist[i+1], wlist[i]
                    
    sort_by_length(words)
    for word in words:
        x = len(word)
        for i in range(2, x):
            if (word[:i] in words) and (word[i:] in words):
                print '{} + {} = {}'.format(word[:i], word[i:], word)
                return
        

                
    
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
        
    print '---------------------------------------------------'
    arr = range(5) + range(5)[::-1]
    m = 6
    print 'm={} smallest of arr={} are={}'.format(m, arr, find_smallest(arr,m))
    
    print '---------------------------------------------------'
    book = 'sam is the best guy there is no person like sam tina agrees'.split(' ')
    print 'book={}'.format(' '.join(book))
    warr = [ ('sam','tina'), ('sam','there'), ('sam','is') ]
    for ws in warr:        
        print 'w1={}, w2={}, min_distance={}'.format(ws[0], ws[1], find_min_distance(book, ws[0], ws[1]))
    
    print '---------------------------------------------------'
    words = [ 'sam', 'tim', 'jackson', 'nolan', 'samjackson4', 'timnolan' ]
    find_longest(words)