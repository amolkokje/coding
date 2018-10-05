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
    print mat
    
    n = len(mat) # rows
    m = len(mat[0]) # cols
    
    def are_equal(arr):
        for k in range(1,len(arr)):
            if arr[0] != arr[k]:
                return False
        return True        
    
    # check rows, cols
    for i in range(n):
        if are_equal(mat[i]) or \
        are_equal([mat[i][x] for x in range(n)]):
            return True
    
    # check diagonals
    if are_equal([mat[i][i] for i in range(n)]) \
    or are_equal([mat[i][x-i] for i in range(n)]):
        return True
    
    return False
    

# 17.3 --> Write an algo that counts the number of trailing zeroes in a factorial    
# every time there is a multiplication by 10, or 5*2, then there is a 0.
# so, count_10 + min(count_2, count_5) = count_0s
## PROBLEM --> still off, come back later - IMPORTANT!

def count_num_zeroes_fact(num):
    c5 = 0
    c2 = 0
    c10 = 0 # 5*2
    
    def find_factors(num, factors_of):
        c = 0
        while num > 0:
            #print num, c
            if num % factors_of == 0:
                c += 1
                num = num/5
            else:
                return c
        return c    
        
    
    while num > 0:
        if num%10 == 0:
            c10 += 1
        
        elif num%5 == 0:
            c5 += find_factors(num, 5)
                
        elif num%2 == 0:
            c2 += find_factors(num, 2)
        
        #print num, count_2, count_5, count_10
        num -= 1    
    
    return c10 + min(c5, c2)
        
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
    
    
if __name__ == '__main__':
    swap_nums(2, 4)
    
    print '---------------------------------------------------'
    mat = []
    mat.append([None,1,1])
    mat.append([1,1,None])
    mat.append([1,None,None])
    print have_winner(mat)
    
    print '---------------------------------------------------'
    a = 50
    print 'Num of zeroes in fact of {} are {}'.format(a, count_num_zeroes_fact(a))
    
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