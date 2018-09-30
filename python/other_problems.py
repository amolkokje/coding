import sys, copy

## Q:: Calculate the number of 2s in numbers from 0-n

def calculate_twos(x):
    count = 0
    print 'Number of 2s in {}:'.format(x)
    x = abs(x)        
    while x >= 1:
        if x%10 == 2:
            count+=1
        x = x/10
    print count

    
## Q:: O(logN) solution to find 2 numbers in an array that sum up to a target value

def two_numbers_sum_target(arr, target):
    """    
    Binary Search approach only works with sorted array and non-repeating elements
    """
    
    def _helper(i, left, right, target):
        if left < right:
            mid = (left+right)/2
            sum = arr[i]+arr[mid]
            if (mid != i) and (sum == target):
                return mid
            if sum > target:
                right=right-1
            elif sum < target:
                left=left+1
            return _helper(i, left, right, target)    

    print 'arr={}, target={}'.format(arr, target)            
    arr_len = len(arr)   
    for i in range(arr_len):
        found = _helper(i, 0, arr_len, target)
        if found:
            return i, found
        
    
## Q:: O(logN) solution to find 3 numbers in an array that sum up to a target value    
    
def three_numbers_sum_target(arr, target):
    print 'arr={}, target={}'.format(arr, target)            
    found_list = []
    arr_len = len(arr)    
    for i in range(arr_len):
        two_sum_target = target - arr[i]
        
        for j in range(arr_len):
            if j != i:
                n1, n2 = two_numbers_sum_target(arr, two_sum_target)
                if n1 and n2:
                    return i, n1, n2
    

## Q:: Find total unique paths from a point in matrix to another point in matrix    
   
def unique_paths(stop_x, stop_y, start_x, start_y, m, n, visited_cells_orig):
    if stop_x == start_x and stop_y == start_y:
        return 1
        
    visited_cells = copy.deepcopy(visited_cells_orig)
    visited_cells[stop_x][stop_y] = True
        
    no_paths = 0
    if stop_x-1 >= 0 and not visited_cells[stop_x-1][stop_y]:
        no_paths += unique_paths(stop_x-1, stop_y, start_x, start_y, m, n, visited_cells)

    if stop_y-1 >= 0 and not visited_cells[stop_x][stop_y-1]:
        no_paths += unique_paths(stop_x, stop_y-1, start_x, start_y, m, n, visited_cells)        
        
    if stop_x+1 < m and not visited_cells[stop_x+1][stop_y]:
        no_paths += unique_paths(stop_x+1, stop_y, start_x, start_y, m, n, visited_cells)

    if stop_y+1 < n and not visited_cells[stop_x][stop_y+1]:
        no_paths += unique_paths(stop_x, stop_y+1, start_x, start_y, m, n, visited_cells)            
    
    return no_paths
   
  
## Q:: Generate permutations of a list

def generate_permutations(ip_list, take_count):
    
    """
    In permutations, order is important. i.e. ABC != CAB
    """
    
    """
    PYTHON ACTUAL USE ---
    from itertools import permutations
    permutations("AMOL", 3) --> will give a list of all permutations, taken 2 at a time
    """
    
    print 'Generating permutations for {}, taking only {} at a time'.format(ip_list, take_count)
    n = len(ip_list)
    visited = [None]*n
    depth = 0
    word = []
    
    def permute(ip_list, word_orig, visited_orig, i):
        """
        ip_list --> input list
        word --> string generated so far
        visited_ --> list of visited cells
        i --> index of cell to visit
        """
        
        if visited_orig[i]:
            return
        
        visited = copy.deepcopy(visited_orig)
        word = copy.deepcopy(word_orig)
        
        word.append(ip_list[i])        
        visited[i] = True
        
        if len(word) == take_count:
            print 'PERMUTATION = {}'.format(''.join(word))
            return
            
        for k in range(n):
            permute(ip_list, word, visited, k)
            
    for i in range(n):
        permute(ip_list, word, visited, i)
        
        
## Q:: Generate permutations of a list        

def generate_combinations(ip_list, take_count):
    
    """
    In combinations, order is not important. i.e. ABC = CAB  --> SUBSETS of a SET
    """
    
    """
    PYTHON ACTUAL USE ---
    from itertools import combinations
    combinations("AMOL", 3) --> will give a list of all combinations, taken 2 at a time
    """
    
    print 'Generating combinations for {}, taking only {} at a time'.format(ip_list, take_count)
    n = len(ip_list)
    visited = [None]*n
    depth = 0
    word = []
    
    def combine(ip_list, word_orig, visited_orig, i):
        """
        ip_list --> input list
        word --> string generated so far
        visited_ --> list of visited cells
        i --> index of cell to visit
        """
        
        if visited_orig[i]:
            return
        
        visited = copy.deepcopy(visited_orig)
        word = copy.deepcopy(word_orig)
        
        word.append(ip_list[i])        
        visited[i] = True
        
        if len(word) == take_count:
            print 'COMBINATION = {}'.format(''.join(word))
            return
            
        # this place is only where there is a difference between permutations and combinations. 
        # in combinations, we don't want to repeat what is already done, so we only move right-side in the array
        for k in range(i+1, n):
            combine(ip_list, word, visited, k)
            
    for i in range(n):
        combine(ip_list, word, visited, i)
        
        
## Q:: find first non-repeating character by iterating through the length of the string only once and by using constant space.        

def find_first_non_repeating_char(ip_string):
    print 'Checking string: {}'.format(ip_string)
    ip_string = list(ip_string)
    n = len(ip_string)
    popped_chars = [None]*n
    for k in range(n):
        check_char = ip_string.pop(0)        
        if not check_char in ip_string and not check_char in popped_chars:
            print '{} is the first char not repeating'.format(check_char)
            break
        popped_chars[k] = check_char
        
        
## Q:: find missing element in an AP        

def ap_find_missing_element(ap):
    # assumption: AP has length greater than 2
    
    # this is precaution just in case the second/third element is the missing one
    diff = min(ap[1]-ap[0], ap[2]-ap[1])
    for i in range(len(ap)-1):
        if ap[i+1] - ap[i] > diff:
            print 'Missing element = {}'.format(ap[i]+diff)


## Q:: Find the largest substring palindrome in a given string. ex: input: abbac output: abba            

def string_find_largest_subset_palindrome(ip_string):
    
    def is_palindrome(s):
        return True if s == s[::-1] else False

    if is_palindrome(ip_string):
        return ip_string
    
    n = window = len(ip_string)
            
    while window > 1:
        for i in range(n-window+1):
            if is_palindrome(ip_string[i:i+window-1]):
                return ip_string[i:i+window-1]
        window-=1    
    

## Q:: Compress aaabbcccc -> a3b2c4

def compress_string(ip_string):
    n = len(ip_string)
    compressed_string = []
    i = 0
    while i < n:
        # match found, special case for last char
        if i+1 < n and ip_string[i] == ip_string[i+1]:
            ch = ip_string[i]
            k = 2
            for j in range(i+2, n):
                if ip_string[j] != ch:
                    break
                k += 1
            
            # append compress chars
            compressed_string += (ch + str(k))
            # move index forward
            i += k            
        else:
            # match not found to compress
            compressed_string += ip_string[i]  
            i += 1 
        
    return ''.join(compressed_string)    

    
if __name__ == '__main__':

    """
    for num in [2, 45546, 1, 0, -3242]:
        calculate_twos(num)
    """

    arr = [2,3,4,5,6,7]
    arr.sort()
    print "-------------------------------------------------------"
    print two_numbers_sum_target(arr, 5)
    
    print "-------------------------------------------------------"
    print three_numbers_sum_target(arr, 12)

    print "-------------------------------------------------------"
    # m-rows, n-cols    
    m = 3
    n = 7
    start_x, start_y = 1, 1
    stop_x, stop_y = 2, 6
    print 'no of paths with matrix {}x{} from ({},{}) to ({},{}) are {}'.format(m,n,start_x,start_y, stop_x,stop_y, unique_paths(stop_x=2, stop_y=6, start_x=1, start_y=1, m=m, n=n, visited_cells_orig=[ [None]*n for _ in range(m) ]))

    print "-------------------------------------------------------"
    # permutations
    ip_word_list = ["AMOL", "AMI"]
    for ip_word in ip_word_list:
        generate_permutations(ip_list=ip_word, take_count=2)
        generate_combinations(ip_list=ip_word, take_count=2)
        
    print "-------------------------------------------------------"    
    find_first_non_repeating_char("molamol") 
    
    print "-------------------------------------------------------"
    ap_find_missing_element([1, 3, 5, 7, 9, 13, 15])
    
    print "-------------------------------------------------------"
    s = "abba"
    print 'largest subset palindrome in string {} is {}'.format(s, string_find_largest_subset_palindrome(s))
    
    print "-------------------------------------------------------"
    string_list = [ "aaabbcccc", "abbccasd" ]
    for s in string_list:
        print 'compressed string for {} is {}'.format(s, compress_string(s)) 