
# Q: Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
                
        return len(nums)
        

# Q: Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).        

def max_profit(prices):
    n = len(prices)
    max = 0
    
    minv = prices[0]
    i = 1
    
    while i < n:
        if prices[i] < minv:
            minv = prices[i]
            i += 1 
            continue
            
        diff = prices[i] - minv
        if diff > max:
            max = diff
        i += 1    
    
    return max
    

# Q: Given an array, rotate the array to the right by k steps, where k is non-negative.
    
def rotate_array(nums, k):
    # put the elements that get pushed out in the front of the arr, and then add the remaining ones
    # elements that will be pushed out on rotation --> arr[n-k:]
    # other elements in the front --> arr[:n-k]
    # put elements in the back, at the front --> arr[n-k:] + arr[:n-k]
    n = len(nums)
    nums[:]= nums[n-k:] + nums[:n-k]
    return nums
    
    
# Q: Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.    

def contains_duplicates(arr):
    return False if len(set(arr)) == len(arr) else True
    # for other languages, put it in a dict, and if exists in a dict, then True
    
    
# Q: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

def single_number(nums):    
    # XOR of a number with itself = 0
    # XOR of a number with any other number X = X
    # so, if xor of all = 0, then no unique element
    # other languages - put in a dict, and then run through the dict    
    
    # SOLUTION - 1
    #xor = 0
    #for num in nums:
    #    xor ^= num
    #return xor
    
    # SOLUTION - 2 -- One liner, and same operation as before
    return reduce(lambda x, y: x ^ y, nums)
    
 
# Q: Given two arrays, write a function to compute their intersection. Each element in the result should appear as many times as it shows in both arrays. The result can be in any order.
# Follow up:
#  What if the given array is already sorted? How would you optimize your algorithm?
#  What if nums1's size is small compared to nums2's size? Which algorithm is better?
#  What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()   
    
    def intersect(smaller, larger):
        n1 = len(smaller)
        n2 = len(larger)
        intersection = []
        for i in range(n1):
            if smaller[i] in larger:
                larger.pop(larger.index(larger[i]))
                intersection.append(smaller[i])
        return intersection   
           
    if len(nums1) > len(nums2):
        return intersect(nums2, nums1)        
    else:
        return intersect(nums1, nums2)   


# Q: Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
        
def plus_one(digits):
    if digits[-1] < 9:
        digits[-1] += 1
    else:
        digits[-1] += 0
        digits[-2] += 1
    return digits
    
    
# Q: Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def move_zeros(nums):
    n = len(nums)    
    i = 0
    
    while i < n:  # length of array will not change here    
        if nums[i] == 0:            
            nums.append(nums.pop(i))
        i += 1
    
# Q: Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#  Each row must contain the digits 1-9 without repetition.
#  Each column must contain the digits 1-9 without repetition.
#  Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.  

def is_sudoku_valid(board):
    # board - 9x9 matrix, containing 9 boxes, each box containing 9 cells
    n = 9
    
    def contains_repeats(arr):
        # checks if thr list contains any repeats
        mod_arr = filter(lambda x:x != '.', arr)
        return False if len(set(mod_arr)) == len(mod_arr) else True
            
    # check rows and cols
    for i in range(n):
        if contains_repeats(board[i]) or contains_repeats([ board[j][i] for j in range(n) ]):
            return False
            
    # check 3x3 boxes        
    for i in range(0,n,3):
        for j in range(0,n,3):
            # convert box elements to arr
            if contains_repeats( board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3] ):
                return False            
        
    
    return True

    
# Q: Given a string, find the length of the longest substring without repeating characters.

def length_longest_substring(s):
        
    def are_chars_repeating(ss):
        d = dict()
        for i in range(len(ss)):
            if ss[i] in d.keys():
                return False
            else:
                d[ss[i]] = 1
        return True

    w = n = len(s) 
    while w > 0:
        print w
        for i in range(n-w+1):
            if are_chars_repeating(s[i:i+w]):
                return w
        w -= 1        
                
    
# Q: There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.    
   
def median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)   # this part will take O(log (m+n))
    n = len(merged)
    mid = n/2  # will default to int i.e. 7/2=3
    if n%2 == 0:          
        return float(merged[mid] + merged[mid+1])/2
    else:
        return merged[mid]
        
# Q: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility); And then read line by line: "PAHNAPLSIIGYIR".
# ----------------
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# ----------------
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

def convert(s, num_rows):
    print 's={}, numRows={}'.format(s, num_rows)
    
    going_down = False  # as the first condition will turn it to true
    n = len(s)
    
    mat = [ [] for _ in range(num_rows) ]
    current_row = 0    
    for i in range(n):
        if current_row == 0 or current_row == (num_rows-1):
            going_down = not going_down
       
        mat[current_row].append(s[i])
        
        if going_down:
            current_row += 1
        else:    
            current_row -= 1

    return reduce(lambda x,y:x+y, mat)
   
# Q: Given a 32-bit signed integer, reverse digits of an integer.

def reverse_int(n):
    sn = str(n)
    if sn[0] == '-':
        return int(sn[0] + sn[:0:-1])
    else:    
        return int(str(n)[::-1])
   
# Q: Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.   
import re, sys
def atoi(ints):
    
    def ret_value(n):
        n = int(n)
        if n > sys.maxint:
            return sys.maxint
        elif n < -sys.maxint:
            return -sys.maxint
        else:
            return n
            
    ints = ints.replace(' ','')
    #print "**{}**".format(ints)
    match = re.match("\d+", ints)
    if match:
        return ret_value(match.group(0))
        
    match = re.match("-\d+", ints)
    if match:
        return ret_value(match.group(0))    
    
    return 0
    
# Q: Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.   
# NOT WORKING !!
  
def regex_match(s, p):
    ns = len(s)
    np = len(p)
    print s, p
    
    cs = cp = 0
    while cp < np:
        if p[cp] == '.':
            print '. START --> cp={}, cs={}'.format(cp, cs)
            while cs < ns:                
                if s[cs] != s[cs-1]:
                    break
                cs += 1
            print '. END --> cs={}'.format(cs)

        elif p[cp] == '*':
            print '* START --> cp={}, cs={}'.format(cp, cs)
            while cs < ns:                
                if s[cs] != s[cs-1]:
                    break
                cs += 1
            print '* END --> cs={}'.format(cs)
                
        
        elif p[cp] != s[cs]:
            print cp, cs
            return False
        
        cp += 1
    
    print cs, cp
    if cs == ns:
        return True
    else:
        return False
            
        
# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:
            
# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   9


# Q:: Write a function that, for two given individuals in our dataset, returns true if and only if they share at least one ancestor.
# Sample input and output:
# parentChildPairs, 3, 8 => false
# parentChildPairs, 5, 8 => true
# parentChildPairs, 6, 8 => true
def have_common_ancestor(pairs, n1, n2):
    # build ancestor map
    ancestor_map = dict()
    for parent, child in pairs:
        if not ancestor_map.get(child):
            ancestor_map[child] = [parent]
        else:
            ancestor_map[child].append(parent)
    #print ancestor_map        
            
    def get_ancestors_tree(child):
        ancestors_tree = list()
        queue = [ child ]        
        while queue:
            x = queue.pop(0)
            if ancestor_map.get(x):
                queue += ancestor_map[x]
            ancestors_tree.append(x)
        # first element is the node itself, so remove it
        return ancestors_tree[1:] 

    n1_ancestors = get_ancestors_tree(n1)
    n2_ancestors = get_ancestors_tree(n2)
    for n in n1_ancestors:
        if n in n2_ancestors:
            return True
    return False
                

# Q: Find out individuals that have 0 and 1 parents.
def get_node_parent_counts_01(pairs):
    """
    pairs -> parent child pairs
    """
    node_parents = dict()
    for pair in pairs:
        # add nodes to the dict, if they do not exist already
        if not node_parents.get(pair[0]):
            node_parents[pair[0]] = 0
            
        if not node_parents.get(pair[1]):
            node_parents[pair[1]] = 0    
            
        node_parents[pair[1]] += 1
    
    output = [ [], [] ]
    for node, parent_count in node_parents.iteritems():
        if parent_count == 0:
            output[0].append(node)
        elif parent_count == 1:
            output[1].append(node)
            
    return output


   
if __name__ == '__main__':
    
    print '--------------------------------------------------------------'
    arrlist = [[1,1,2], [0,0,1,1,1,2,2,3,3,4]] 
    for arr in arrlist:
        print 'arr={}'.format(arr) 
        print 'final={}'.format(removeDuplicates(arr))
        
    print '--------------------------------------------------------------'
    arrlist = [[7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1]] 
    for arr in arrlist:
        print 'prices={}, max_profit={}'.format(arr, max_profit(arr))
        
    print '--------------------------------------------------------------'
    arrlist = [([1,2,3,4,5,6,7], 3), ([-1,-100,3,99], 2), (range(20), 2)] 
    for arr in arrlist:
        print 'arr={}, k={}'.format(arr[0], arr[1])
        print 'rotated={}'.format(rotate_array(arr[0], arr[1]))
        
    print '--------------------------------------------------------------'
    arrlist = [[1,2,3,1], [1,2,3,4,5], [1,1,1,3,3,4,3,2,4,2]] 
    for arr in arrlist:
        print 'arr={}, contains_duplicates={}'.format(arr, contains_duplicates(arr)) 

    print '--------------------------------------------------------------'
    arrlist = [[2,1,2], [4,1,2,2,1]] 
    for arr in arrlist:
        print 'arr={}, single_number={}'.format(arr, single_number(arr)) 
        
    print '--------------------------------------------------------------'
    nums1 = [1,2,2,1]
    nums2 = [2,2]   
    print 'nums1={}, nums2={}'.format(nums1, nums2)
    print '-- intersection={}'.format(intersection(nums1, nums2))
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]   
    print 'nums1={}, nums2={}'.format(nums1, nums2)
    print '-- intersection={}'.format(intersection(nums1, nums2))
    
    print '--------------------------------------------------------------'
    arrlist = [[1,2,3], [4,3,2,1]] 
    for arr in arrlist:
        print 'digits={}'.format(arr) 
        print '-- plus_one={}'.format(plus_one(arr)) 
        
    print '--------------------------------------------------------------'
    arrlist = [[0,1,0,3,12]] 
    for arr in arrlist:
        print 'arr={}'.format(arr) 
        move_zeros(arr)
        print '-- move_zeros={}'.format(arr)       

    
    print '--------------------------------------------------------------'
    board_list = [    
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]    
    ]
    for board in board_list:
        print 'is_sudoku_valid={}'.format(is_sudoku_valid(board))
        
        
    print '--------------------------------------------------------------'
    arrlist = [ "abcabcbb" , "bbbbb", "pwwkew"] 
    for arr in arrlist:
        print 's={}, length of longest substring={}'.format(arr, length_longest_substring(arr))
        
    print '--------------------------------------------------------------'
    nums1 = [1, 3]
    nums2 = [2]
    print 'nums1={}, nums2={}, median={}'.format(nums1, nums2, median_sorted_arrays(nums1, nums2))     
    nums1 = [1, 2]
    nums2 = [3, 4]
    print 'nums1={}, nums2={}, median={}'.format(nums1, nums2, median_sorted_arrays(nums1, nums2))     
        
    print '--------------------------------------------------------------'
    arrlist = [ ("PAYPALISHIRING",3), ("PAYPALISHIRING",4)]
    for arr in arrlist:
        print ''.join(convert(arr[0], arr[1]))
        
    print '--------------------------------------------------------------'
    nlist = [ 123, -123, 120]
    for n in nlist:
        print 'n={}, reverse={}'.format(n, reverse_int(n))
        
    print '--------------------------------------------------------------'
    nlist = [ "42", "   -42", "4193 with words", "words and 987", "-91283472332"]
    for n in nlist:
        print 'n={}, atoi={}'.format(n, atoi(n))

    """ NOT WORKING !    
    print '--------------------------------------------------------------'
    iplist = [ ("aa","a"), ("aa","a*"), ("ab",".*"), ("aab","c*a*b"), ("mississippi","mis*is*p*.")]
    for ip in iplist:
        print 'regex.match({},{}) = {}'.format(ip[0], ip[1], regex_match(ip[0],ip[1]))
    """    
                
    print '--------------------------------------------------------------'
    parent_child_pairs = [
        (1, 3), (2, 3), (3, 6), (5, 6),
        (5, 7), (4, 5), (4, 8), (8, 9)
    ]
    print 'Children with 0 or 1 parents = {}'.format(get_node_parent_counts_01(parent_child_pairs))
    pairs = [ (3,8), (5,8), (6,8) ]
    for pair in pairs:
        print '{} and {} have common ancestor = {}'.format(pair[0], pair[1], have_common_ancestor(parent_child_pairs, pair[0], pair[1]))
    