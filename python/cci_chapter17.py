# 17.1 -> swapping number in place, without temp vars
def swap_nums(a, b):
    print 'before: a={}, b={}'.format(a, b)
    a, b = b, a
    print 'after: a={}, b={}'.format(a, b)
    
# 17.2 -> Design an algorithm to find out if someone has won a game of tic-tac-toe    
# always a 3x3 matrix, but this solution works for NxN matrix with any symbols

def have_winner(mat):
    """
    None -> no value in cell
    """
    n = len(mat) # rows=cols
    
    def are_equal(arr):
        # if no value is a number and not None
        #return True if reduce( lambda x,y:x^y, arr) == 0 else False
        for k in range(1,len(arr)):
            if arr[0] != arr[k]:
                return False
        return True        
    
    # check rows, cols
    for i in range(n):
        if are_equal(mat[i]) or \
        are_equal([mat[j][i] for j in range(n)]):
            return True
    
    # check diagonals
    if are_equal([mat[i][i] for i in range(n)]) \
    or are_equal([mat[i][(n-1)-i] for i in range(n)]):  # because n=3, but max index=2
        return True
    
    return False
    

# 17.3 --> Write an algo that counts the number of trailing zeroes in a factorial    
# every time there is a multiplication by 10, or 5*2, then there is a 0.
# so, count_10 + min(count_2, count_5) = count_0s

# EXPLANATION - https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
def count_num_zeroes_fact(num):
    
    def find_factors_5(x):
        c = 0
        # going only till 5, as no factors of 5 below that
        while x > 4:
            if x%5 == 0:
                c += 1
                x = x/5
            else: 
                break
        return c        
        
    c0 = 0
    # going only till 5, as no factors of 5 below that. If some other case, go lower
    while num > 4:
        c0 += find_factors_5(num)
        num -= 1
                
    return c0  
            

def memoize(func):    

    class mdict(dict):
        def __missing__(self, key):
            self[key] = func(key)
            return self[key]
      
    return mdict().__getitem__

@memoize    
def find_fact_trailing_zeros(n):
    
    @memoize
    def fact(x):
        if x == 0 or x == 1:
            return 1
        else:
            return x*fact(x-1)    
        
    factn = str(fact(n))
    i = len(factn)-1
    c = 0
    while i > 0:
        if int(factn[i]) != 0:
            return c
        else:
            c += 1
        i -= 1    
    
    return c    
            
    
 
# 17.4 --> find max of two numbers without using comparison operator
# bitwise operation - try later


# 17.5 --> Master Mind game hits and pseudo-hits

def get_hits(actual, guess):
    # length of actual and guess will always be the same
    n = len(actual)
    
    hits = {}
    pseudo_hits = {}
    
    # hits
    for i in range(n):
        if actual[i] == guess[i]:
            hits[i] = actual[i]
    
    # guess loop
    for g in range(n):
        # actual loop
        for a in range(n):
            # pseudo hit --> value equal, but index not; not already hit/pseudo_hit
            if g != a and guess[g] == actual[a] and a not in hits.keys() and a not in pseudo_hits.keys():
                pseudo_hits[a] = actual[a]
                    
    return 'hits={}, pseudo-hits={}'.format(len(hits), len(pseudo_hits))
    
# 17.6 --> Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n, 
# the entire array would be sorted. Minimize n - m (that is, find the smallest such sequence).
# e.g. [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] --> m=3, n=10

def find_index_to_sort(arr):
    n = len(arr)
    
    def find_left():
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return i+1
    
    def find_right():
        for i in range(n-1, 1, -1):
            if arr[i] < arr[i-1]:
                return i-1           

    def shrink_left(left, right):
        while left >= 0:
            left_max = max(arr[:left+1])
            middle_min = min(arr[left:right])
            if left_max <= middle_min:
                return left
            else:
                left -= 1
    
    def shrink_right(left, right):
        while right < n:
            right_min = min(arr[right:])
            middle_max = max(arr[left:right])
            if right_min >= middle_max:
                return right
            else:
                right += 1

    left = find_left() 
    right = find_right()  
    m = shrink_left( left, right ) 
    n = shrink_right( left, right )
    print 'arr={}, Sort from m={} to n={}'.format(arr, m, n)
    
# 17.7 --> Given any integer, print an English phrase that describes the integer (e.g., "One Thousand, Two Hundred Thirty Four").

num_map = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }

    
def num_string(num):
    
    def get_tens(n):
        ns = str(n)
        if int(ns[-1]) == 0:
            return num_map[num]
        else:
            return num_map[int(ns[0])*10] + num_map[int(ns[1])]
    
    def get_hundreds(n):
        ns = str(n)
        if int(ns[-2:]) == 0:
            return num_map[int(ns[0])] + ' hundred '
        else:
            return num_map[int(ns[0])] + ' hundred ' + get_tens(int(ns[1:]))
            
    def get_thousands(n):
        ns = str(n)
        if int(ns[-3:]) == 0:
            return num_map[int(ns[0])] + ' thousand '
        else:
            return num_map[int(ns[0])] + ' thousand ' + get_hundreds(int(ns[1:]))
    
    if num < 20:
        return num_map[num]
    elif 20 <= num < 100:
        return get_tens(num)
    elif 100 <= num < 1000:
        return get_hundreds(num)
    elif num >= 1000:    
        return get_thousands(num)
 
 
    
# 17.8 --> You are given an array of integers (both positive and negative). Find the contiguous sequence with the
# largest sum. Return the sum. EXAMPLE
# Input: 2, -8, 3, -2, 4, -10
# Output 5 i.e. {3, -2, 4}


def get_contiguous_sequence_max_sum(arr):
    tstart = 0  # temp var to store start
    sum = 0  # temp var to store sum

    # final values
    start = 0
    stop = 0
    maxsum = 0

    n = len(arr)

    for i in range(n):
        sum += arr[i]

        # if =0 means starting fresh, so reset
        # if <0 means decreasing, so reset
        if sum <= 0:
            sum = 0
            if i+1 < n:
                tstart = i+1  # reset start pointer

        # if sum crosses max, use temp var to update the final values
        if sum > maxsum:
            start = tstart
            stop = i
            maxsum = sum

    return arr[start:stop+1]


# 17.9 ->  Design a method to find the frequency of occurrences of any given word in a book
# simple dict, so skip


# 17.10 -> For example, the following XML might be converted into the compressed string below
# (assuming a mapping off family -> l, person ->2, firstName -> 3, LastName -> 4, state -> 5).
# <family lastName="McDowell" state="CA"> 
#     <person firstName="Gayle">Some Message</person> 
# </family>
# Becomes:
# 1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0
# Write code to print the encoded version of an XML element (passed in E Lament and Attribute objects).
"""
PSEUDO-CODE:

TAG = {
    'family': 1,
    'person': 2
}

ATT = {
    'firstName': 3,
    'lastName': 4,
    'state': 5
}

def process_atts(att_name_val_dict):
    out = ''
    for name, val for att_name_val_dict.iteritems():
        out += '{} {}'.format(ATT[name], val)
    return out    

def process_line(out, line):
    tag, atts = get_tag_atts(line)
    if tag:
        out += process_tag(tag)
    if atts:
        out += process_atts(atts)
    if tag and tag_has_closing(line):
        out += ' 0'            
    return out

# MAIN
out = ''
for line in xml_file_line:
    process_line(out, line)  
""" 
## AMOL -> SOME THING IS WEIRD!
  
import xml.etree.ElementTree as ET
   
def encode_xml_string(xml):
    print xml
    encoded_string = []
    
    map = {
        'family':1,
        'person':2,
        'firstName':3, 
        'lastName':4,
        'state':5       
    }
        
    def get_children(ele):
        return ele.__children
        
    
    def encode_tag(ele):
        print ele
        if not ele:
            encoded_string += ' {}'.format(map[ele.tag])
            for attr, val in ele.attrib:
                encoded_string += ' {}'.format(map[attr])
            encoded_string += ' 0 '    
            print encoded_string
            
    
    root = ET.fromstring(xml)
    queue = [root]
    while not queue:
        print queue
        ele = queue.pop(0)
        if ele:
            encode_tag(ele)
            for child in get_children(ele):
                queue.append(child)
                
    print encoded_string            
    
    
# 17.11 -> Implement a method rand7 given rand5 - That is, given a method that generates a random number between 0 and 4 (inclusive), write a method that generates a random number between 0 and 6 (inclusive).
# NOTE: the solution is not the same as its in the book, but I think this one is property

import random

def rand7():
    
    def rand5():
        return random.randint(0, 5)
        
    return (rand5()*7)/5
    
 
# 17.12 -> Design an algorithm to find all pairs of integers within an array which sum to a specified values
            
def find_pairs_sum(arr, sum):
    # O(N)
    pairs_list = list()
    sum_dict = dict()
    for a in arr:
        if sum_dict.get(sum-a) and ([a, sum-a] not in pairs_list) and ([sum-a, a] not in pairs_list):
            pairs_list.append([a, sum-a])
        else:
            sum_dict[a] = sum-a
    return pairs_list
    
 

# 17.13 -> Consider a simple node-like data structure called BiNode, which has pointers to two other nodes.
# The data structure BiNode could be used to represent both a binary tree (where node1 is the left node and node2
# is the right node) or a doubly linked list (where node1 is the previous node and node2 is the next node). Implement
# a method to convert a binary search tree (implemented with BiNode) into a doubly linked list. The values should be
# kept in order and the operation should be performed in place (that is, on the original data structure).
## AMOL - SEEMS TOO COMPLEX
    

# 17.4 ->  Oh, no! You have just completed a lengthy document when you have an unfortunate Find/Replace mishap. You
# have accidentally removed all spaces, punctuation, and capitalization in the document. A sentence like "I reset the
# computer. It still didn't boot!" would become "iresetthecomputeritstilldidntboot". You figure that you can add back
# in the punctation and capitalization later, once you get the individual words properly separated. Most of the words
# will be in a dictionary, but some strings, like proper names, will not.
# Given a dictionary (a list of words), design an algorithm to find the optimal way of "unconcatenating" a sequence of
# words. In this case, "optimal" is defined to be the parsing which minimizes the number of unrecognized sequences of
# characters.
# For example, the string "jesslookedjustliketimherbrother" would be optimally parsed as "JESS looked just like TIM
# her brother". This parsing has seven unrecognized characters, which we have capitalized for clarity.
## AMOL - not optimal, INCORRECT?? - TRY TO UNDERSTAND BOOK SOLUTION!

# OPTIMIZATION - put all words of dictionary in a trie, so can skip iteration quickly if a word is not found


def add_spaces(olds, word_dictionary):
    news = []
    n = len(olds)
    
    def get_word_end(i, j, word_dictionary):
        w = (j-i)-1 # window size
        while w > 0:
            word = olds[j-w:j]
            if word in word_dictionary:
                return word
            w -= 1    

    i = 0        
    while i < n:
        print 'i={}'.format(i)
    
        j = i+1
        while i+1 <= j <= n:  ## NOTE: range(min, max) --> index from [min:max-1] i.e. last is not included
            word = olds[i:j]  ## NOTE: Here, last is not included
            #print 'i={}:j={}: word={}'.format(i, j, word)
            
            if word in word_dictionary:
                #print 'START={}'.format(word)
                news.append(word)
                i += (j-i)

            # AMOL - why checking the same substring again for word_end?    
            word_end = get_word_end(i, j, word_dictionary)
            if word_end:
                print 'END={} in word={}'.format(word_end, word)
                news.append(word.split(word_end)[0].upper())
                news.append(word_end)
                i += (j-i)
            
            j += 1
            
        i += 1        
                
    return news            
                
 
# Q: Google Sample Question --> Given an array and a number, check if there are two elements in the array that sum to
# the number
# [ 1, 2, 3, 4 ], Sum=8 --> No
# [ 1, 2, 4, 4 ], Sum=8 --> Yes
# Reference: https://youtu.be/XKu_SEDAykw

def sum_exists(arr, sum):
    sum_map = dict()
    for a in arr:
        if sum_map.get(sum-a):
            return True
        else:
            sum_map[a] = sum-a
    return False
 
 
 
if __name__ == '__main__':
    swap_nums(2, 4)
    
    print '---------------------------------------------------'
    mat = []
    mat.append([None,1,1])
    mat.append([1,1,None])
    mat.append([1,None,None])
    print 'mat={}, have_winner={}'.format(mat, have_winner(mat))
    
    print '---------------------------------------------------'
    alist = [6, 15, 50, 70]
    for a in alist:
        print 'Num of trailing zeroes in fact of {} are {}, {}'.format(a, find_fact_trailing_zeros(a), count_num_zeroes_fact(a))
    
    print '---------------------------------------------------'
    actual = 'RGBY'
    guess = 'GGRR'
    print 'MM actual={}, guess={}, {}'.format(actual, guess, get_hits(actual, guess))
    actual = 'RGGY'
    guess = 'GGRR'
    print 'MM actual={}, guess={}, {}'.format(actual, guess, get_hits(actual, guess))
    
    print '---------------------------------------------------'
    num_list = [3, 24, 23, 123, 223, 3445, 33456, 333456]
    for num in num_list:
        print 'Number={}, String={}'.format(num, num_string(num) )
        
    print '---------------------------------------------------'
    arrlist = [ [2,-8,3,-2,4,-10], [2,3,-8,-1,2,4,-2,3], [2,3,-8,8], [2,3,0,4], [ 2, 2, 2, -8, 1, 1, 1 ] ]
    for arr in arrlist:
        print 'Contiguous sequence with max sum for {} is {}'.format(arr, get_contiguous_sequence_max_sum(arr))
        
    print '---------------------------------------------------'    
    ss = """
    <family lastName="McDowell" state="CA"> 
        <person firstName="Gayle">Some Message</person> 
    </family>
    """ 
    encode_xml_string(ss)
    
    print '---------------------------------------------------'    
    rand7list = []
    for _ in range(20):
        rand7list.append(rand7())
    print rand7list    
    
    print '---------------------------------------------------'    
    arrlist = [ [-2,-1,0,3,5,6,7,9,13,14] ]
    sum = 5
    for arr in arrlist:
        print '{}: pairs with sum={} are: {}'.format(arr, sum, find_pairs_sum(arr, sum))
        
    print '---------------------------------------------------'        
    word_dictionary = [ 'looked', 'just', 'like', 'her', 'brother', 'I', 'reset', 'computer', 'It', 'still', 'didn\'t', 'boot' ]
    sentence = 'jesslookedjustliketimherbrother'
    print 'original={}, with_spaces={}'.format(sentence, add_spaces(sentence, word_dictionary))
    
    word_dictionary =  [ 'i', 'reset', 'the', 'computer', 'it', 'still', 'didnt', 'boot' ]
    sentence = 'iresetthecomputeritstilldidntboot'
    print 'original={}, with_spaces={}'.format(sentence, add_spaces(sentence, word_dictionary))

    print '---------------------------------------------------'        
    arr = [ 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19 ]
    print find_index_to_sort(arr)
    
    print '---------------------------------------------------'        
    arrlist = [ [1,2,3,4], [1,2,4,4] ]
    sum = 8
    for arr in arrlist:
        print 'sum={}, arr={}, sum_exists={}'.format(sum, arr, sum_exists(arr, sum))