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
        while x > 0:
            if x%5 == 0:
                c += 1
                x = x/5
            else:
                return c        
        
    c0 = 0
    while num > 1:
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
    hi = []
    # length of actual and guess will always be the same
    n = len(actual)
    h = 0
    ph = 0
    # hits
    for i in range(n):
        if actual[i] == guess[i]:
            hi.append(i)
            h += 1
        
    # pseudo-hits        
    psi = []
    for i in range(n):
        # Check 4 conditions:
        # 1- index already not hit
        # 2- element in guess exists in actual
        # 3- get the index of the guess element in the actual. And see if it is already not hit
        # 4- get the index of the first element in guess which is the same value, and see if it is already not covered in pseudo-hits
        if (not i in hi) and (guess[i] in actual):
            if (not actual.index(guess[i]) in hi) and (not guess.index(guess[i]) in psi):
                ph += 1
                psi.append(i)                        
    
    return 'hits={}, pseudo-hits={}'.format(h, ph)

# 17.6 --> Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n, 
# the entire array would be sorted. Minimize n - m (that is, find the smallest such sequence).
## --> UNABLE TO UNDERSTAND HOW TO SOLVE


# 17.7 --> Given any integer, print an English phrase that describes the integer (e.g., "One Thousand, Two Hundred Thirty Four").

def print_num_string(num):
	
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
    
    num_str = str(num)
    num_arr = [ num_str[i] for i in range(len(num_str)) ]
    print num_arr
    
    def get_tens(num_arr):
        # 10 <= num < 100
        print 'get_tens = {}'.format(num_arr)
        num_string = []
        if int(num_arr[0]) == 1:
            return num_map[int(''.join(num_arr))]
        else:
            num_string.append(num_map[int(num_arr[0])*10])
            num_string.append(num_map[int(num_arr[1])])
            return num_string
            
    def get_hundreds(num_arr):
        # 100 <= num < 1000
        print 'get_hundreds = {}'.format(num_arr)
        num_string = []
        num_string.append(num_map[int(num_arr[0])])
        num_string.append('hundred')
        return num_string + get_tens(num_arr[1:])
        
    def get_thousands(num_arr):
        # 1000 <= num < 10000
        print 'get_thousands = {}'.format(num_arr)
        num_string = []
        n = len(num_arr)
        print 'n={}'.format(n)
        if n == 4: # 3,456
            num_string += num_map[int(num_arr[0])]
        elif n == 5: # 33,456     
            num_string +=  get_tens(num_arr[0:2])
        elif n == 6:
            num_string += get_hundreds(num_arr[0:3])
            
        num_string.append('thousand,')
        if n == 5:
            return num_string + get_hundreds(num_arr[2:])
        elif n == 6:
            return num_string + get_hundreds(num_arr[3:])
        
    num_string = []
    if num < 10:
        return num_map[int(num)]
    elif 10 <= num < 100:
        return get_tens(num_arr)
    elif 100 <= num < 1000:
        return get_hundreds(num_arr)
    elif 1000 <= num:
        return get_thousands(num_arr)    
	
    
    
# 17.8 --> You are given an array of integers (both positive and negative). Find the contiguous sequence with the largest sum. Return the sum. EXAMPLE
# Input: 2, -8, 3, -2, 4, -10
# Output 5 i.e. {3, -2, 4}


def get_contiguous_sequence_max_sum(arr):
    
    start = stop = 0 # final
    tstart = tstop = 0 # temp current values
    sum = 0
    max = None  
    
    for i in range(len(arr)):
        # sum is never 0, unless explicitly set
        if sum == 0:
            start = i
        
        sum += arr[i]        
        
        if sum > max:
            stop = i
            max = sum
        
        # if sum<0, then we are decreasing, so start again
        elif sum < 0:
            sum = 0
            
    return arr[start:stop+1]        

# 17.9 ->  Design a method to find the frequency of occurrences of any given word in a book
# simple dict, so skip


# 17.10 -> For example, the following XML might be converted into the compressed string below (assuming a mapping off family -> l, person ->2, frstName -> 3, LastName -> 4, state -> 5).
# <family lastName="McDowell" state="CA"> 
#     <person firstName="Gayle">Some Message</person> 
# </family>
# Becomes:
# 1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0
# Write code to print the encoded version of an XML element (passed in E Lament and Attribute objects).
  
## AMOL -> UNABLE TO FIGURE OUT THE PYTHON LIB
  
import xml.etree.ElementTree as ET
   
def encode_xml_string(xml):
    encoded_string = []
    
    map_attr = {
        'family':1,
        'person':2,
        'firstName':3, 
        'lastName':4,
        'state':5       
    }
    
    et = ET.fromstring(xml)
    
   # for item in et.items():
   #     print item.tail
        
    for item in et:
        print item.tag, item.attrib, item.tail
    
    for tag in et.items():
        encoded_string.append('{} {}'.format(map_attr[tag[0]],tag[1]))
        encoded_string.append('0')
        
       # print encoded_string
    # split by >< to get xml tags
    
    # encode attributes and values within each tags
    

# 17.11 -> Implement a method rand70 given randSQ- That is, given a method that generates a random number between 0 and 4 (inclusive), write a method that generates a random number between 0 and 6 (inclusive).
# NOTE: the solution is not the same as its in the book, but I think this one is property

import random

def rand7():
    
    def rand5():
        return random.randint(0, 5)
        
    return (rand5()*7)/5
    
 
# 17.12 ->  Design an algorithm to find all pairs of integers within an array which sum to a specified values

def bs_val(arr, v):
    """
    binary search to find a value
    """
    
    def bsr(arr, v, l, r):
        if l < r:
            m = (l+r)/2
            if arr[m] == v:
                return True
            elif arr[m] > v:
                return bsr(arr, v, l, m-1)
            else:
                return bsr(arr, v, m+1, r)

    return bsr(arr, v, 0, len(arr)) 
    
                
def find_pairs_sum(arr, sum):
    found_pairs = []    
    arr.sort()
    
    for i in range(len(arr)):
        
        element_find = sum - arr[i]
        
        if bs_val(arr, element_find):
            pair = [arr[i], element_find]
            pair.sort()
            
            if not pair in found_pairs:  
                found_pairs.append(pair)
                
    return found_pairs            
 

# 17.13 -> Consider a simple node-like data structure called BiNode, which has pointers to two other nodes. The data structure BiNode could be used to represent both a binary tree (where nodel is the left node and node2 is the right node) or a doubly linked list (where nodel is the previous node and node2 is the next node). Implement a method to convert a binary search tree (implemented with BiNode) into a doubly linked list. The values should be kept in order and the operation should be performed in place (that is, on the original data structure). 
## AMOL - SEEMS TOO COMPLEX


# 17.4 ->  Oh, no! You have just completed a lengthy document when you have an unfortunate Find/Replace mishap. You have accidentally removed all spaces, punctuation, and capitalization in the document. A sentence like "I reset the computer. It still didn't boot!" would become "iresetthecomputeritstilldidntboot". You figure that you can add back in the punctation and capitalization later, once you get the individual words properly separated. Most of the words will be in a dictionary, but some strings, like proper names, will not.
# Given a dictionary (a list of words), design an algorithm to find the optimal way of "unconcatenating" a sequence of words. In this case, "optimal" is defined to be the parsing which minimizes the number of unrecognized sequences of characters.
# For example, the string "jesslookedjustliketimherbrother" would be optimally parsed as "JESS looked just like TIM her brother". This parsing has seven unrecognized characters, which we have capitalized for clarity.



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
            word = olds[i:j]  ## NOTE: Here, last is included
            print 'i={}:j={}: word={}'.format(i, j, word)
            
            if word in word_dictionary:
                print 'START={}'.format(word)
                news.append(word)
                i += (j-i)

            word_end = get_word_end(i, j, word_dictionary)
            if word_end:
                print 'END={} in word={}'.format(word_end, word)
                news.append(word.split(word_end)[0].upper())
                news.append(word_end)
                i += (j-i)
            
            j += 1
            
        i += 1        
                
    return news            
                
                
 
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
        print 'Num of zeroes in fact of {} are {}, {}'.format(a, find_fact_trailing_zeros(a), count_num_zeroes_fact(a))
    
    print '---------------------------------------------------'
    actual = 'RGBY'
    guess = 'GGRR'
    print 'MM actual={}, guess={}, {}'.format(actual, guess, get_hits(actual, guess))
    
    print '---------------------------------------------------'
    num_list = [3, 24, 23, 123, 223, 3445, 33456, 333456]
    for num in num_list:
        print 'Number={}, String={}'.format(num, print_num_string(num) )
        
    print '---------------------------------------------------'
    arrlist = [ [2,-8,3,-2,4,-10], [2,3,-8,-1,2,4,-2,3], [2,3,-8,8], [2,3,0,4] ]
    for arr in arrlist:
        print 'Contiguous sequence with max sum for {} is {}'.format(arr, get_contiguous_sequence_max_sum(arr))
        
    print '---------------------------------------------------'    
    ss = """
    <family lastName="McDowell" state="CA"> 
        <person firstName="Gayle">Some Message</person> 
    </family>
    """ 
    ##encode_xml_string(ss)
    
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