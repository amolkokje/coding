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
    
if __name__ == '__main__':
    swap_nums(2, 4)
    
    print '---------------------------------------------------'
    mat = []
    mat.append([None, 1, 1])
    mat.append([1,1,None])
    mat.append([1, None, None])
    print have_winner(mat)
    
    print '---------------------------------------------------'
    a = 50
    print 'Num of zeroes in fact of {} are {}'.format(a, count_num_zeroes_fact(a))
    
    print '---------------------------------------------------'
    actual = 'RGBY'
    guess = 'GGRR'
    print 'MM actual={}, guess={}, {}'.format(actual, guess, get_hits(actual, guess))