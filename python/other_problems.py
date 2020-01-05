import sys, copy


## Q:: Calculate the number of 2s in numbers from 0-n

def memoize(func):
    class memodict(dict):
        def __missing__(self, key):
            self[key] = func(key)
            return self[key]

    return memodict().__getitem__


def calculate_two(x):
    @memoize
    def _count_two(x):
        if x > 0:
            return len(filter(lambda x: x == 2, [int(d) for d in str(x)])) + _count_two(x - 1)
        else:
            return 0

    return _count_two(abs(x))


## Q:: O(logN) solution to find 2 numbers in an array that sum up to a target value

def two_numbers_sum_target(arr, target):
    ## O(N) approach - for any type of elements
    d = dict()
    for a in arr:
        # if 'target-element' exists in dict, then the 2 elements are found
        if d.get(target - a):
            return a, target - a

        elif not d.get(a):
            # store as 'element': 'target-element', if does not already exist
            d[a] = target - a


            ## O(logN) approach - only for sorted, non-repeating arrays
            # def _helper(i, left, right, target):
            #    if left < right:
            #        mid = (left+right)/2
            #        sum = arr[i]+arr[mid]
            #        if (mid != i) and (sum == target):
            #            return mid
            #        if sum > target:
            #            right=right-1
            #        elif sum < target:
            #            left=left+1
            #        return _helper(i, left, right, target)
            #
            # print 'arr={}, target={}'.format(arr, target)
            # arr_len = len(arr)
            # for i in range(arr_len):
            #    found = _helper(i, 0, arr_len, target)
            #    if found:
            #        return i, found


## Q:: O(logN) solution to find 3 numbers in an array that sum up to a target value    

def three_numbers_sum_target(arr, target):
    print 'arr={}, target={}'.format(arr, target)
    found_list = []
    arr_len = len(arr)
    for i in range(arr_len):
        two_sum_target = target - arr[i]

        for j in range(arr_len):
            if j != i:
                # will be O(N^2) or O(N.LogN) based on two_numbers_sum_target()
                n1, n2 = two_numbers_sum_target(arr, two_sum_target)
                if n1 and n2:
                    return i, n1, n2


## Q:: Find total unique paths from a point in matrix to another point in matrix  --> SEE memoize.py

def unique_paths(stop_x, stop_y, start_x, start_y, m, n, visited_cells_orig):
    if stop_x == start_x and stop_y == start_y:
        return 1

    visited_cells = copy.deepcopy(visited_cells_orig)
    visited_cells[stop_x][stop_y] = True

    no_paths = 0
    if stop_x - 1 >= 0 and not visited_cells[stop_x - 1][stop_y]:
        no_paths += unique_paths(stop_x - 1, stop_y, start_x, start_y, m, n, visited_cells)

    if stop_y - 1 >= 0 and not visited_cells[stop_x][stop_y - 1]:
        no_paths += unique_paths(stop_x, stop_y - 1, start_x, start_y, m, n, visited_cells)

    if stop_x + 1 < m and not visited_cells[stop_x + 1][stop_y]:
        no_paths += unique_paths(stop_x + 1, stop_y, start_x, start_y, m, n, visited_cells)

    if stop_y + 1 < n and not visited_cells[stop_x][stop_y + 1]:
        no_paths += unique_paths(stop_x, stop_y + 1, start_x, start_y, m, n, visited_cells)

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
    visited = [None] * n
    depth = 0
    word = []

    def permute(word_orig, visited_orig, i):
        """        
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
            permute(word, visited, k)

    for i in range(n):
        permute(word, visited, i)


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
    visited = [None] * n
    depth = 0
    word = []

    def combine(word_orig, visited_orig, i):
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
        for k in range(i + 1, n):
            combine(word, visited, k)

    for i in range(n):
        combine(word, visited, i)


## Q:: find first non-repeating character by iterating through the length of the string only once and by using constant
# space. Below approach goes through the string 2 times
# for one time, also store position of first occurence in the dict. And then, at end, run through the dict elements
# instead of the list to find the element with count=1 that occurs first.
# Reference:https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/

## CONSTANT SPACE
def find_first_non_repeating_char(ip_string):
    # populate array with 0 for all possible chars
    arr = [0 for _ in range(ord('z'))]

    # if a char is found in string, increment the counter
    for s in ip_string:
        arr[ord(s)] += 1

    # if char is found only once, return that char        
    for s in ip_string:
        if arr[ord(s)] == 1:
            return s


## SPACE DEPENDS ON CHARS IN THE STRING - Pythonic
def find_first_non_repeating_char_2(ipstring):
    found_dict = dict()

    for c in ipstring:
        if found_dict.get(c):
            found_dict[c] += 1
        else:
            found_dict[c] = 1

    for c in ipstring:
        if found_dict[c] == 1:
            return c


## Q:: find missing element in an AP        

def ap_find_missing_element(ap):
    # assumption: AP has length greater than 2

    # this is precaution just in case the second/third element is the missing one
    diff = min(ap[1] - ap[0], ap[2] - ap[1])
    for i in range(len(ap) - 1):
        if ap[i + 1] - ap[i] != diff:
            missing_element = ap[i] + diff
            print 'Missing element = {}'.format(missing_element)
            return missing_element


## Q:: Find the largest substring palindrome in a given string. ex: input: abbac output: abba

def string_find_largest_subset_palindrome(ip_string):
    def _is_palindrome(s):
        return True if s == s[::-1] else False

    n = window = len(ip_string)

    while window > 1:
        for i in range(n - window + 1):  # does not include the last value
            s = ip_string[i:i + window]  # does not include the last value
            if _is_palindrome(s):
                return s
        window -= 1


## Q:: Compress aaabbcccc -> a3b2c4

def compress_string(ip_string):
    n = len(ip_string)
    compresssed = ''
    i = 0

    def _compress_str(append_to, chr, count):
        """ helper method to generate compressed string """
        if count > 1:
            return append_to + chr + str(count)
        else:
            return append_to + chr

    while i < n - 1:
        c = 1  # to maintain compress count
        j = i + 1  # index to navigate successive places to determine degree of compression

        while j < n:
            if ip_string[j] == ip_string[i]:
                # if there is a match, increment and continue
                c += 1
                j += 1
                if j == n:  # special case when the index 'j' reaches end of string
                    # if reached end of string, return whatever has been reached so far
                    return _compress_str(compresssed, ip_string[i], c)

            else:
                # if there is no match, compress and move the index forward
                compresssed = _compress_str(compresssed, ip_string[i], c)
                i += c
                break

    if i == n - 1:
        # this case is reached when index 'n' and 'n-1' are not the same
        return compresssed + ip_string[i]


## Q:: implement without using python Contains() or find()

def does_string_contain_substring(main, sub):
    """
    main -> string to look in
    sub -> string to look for    
    """
    m = len(main)
    s = len(sub)

    if m == s and main == sub:
        return True

    for i in range(m - s + 1):
        if main[i:i + s] == sub:
            return True

    return False


## Q:: Next closest bigger number with the same digits. You have to create a function that takes a positive integer number and 
## returns the next bigger number formed by the same digits:
# next_bigger(12)==21
# next_bigger(513)==531
# next_bigger(2017)==2071
# next_bigger(4132)==4213
## If no bigger number can be composed using those digits, return -1:
# next_bigger(9)==-1
# next_bigger(111)==-1
# next_bigger(531)==-1

def next_bigger(num):
    # convert to list of integers
    nums = [int(n) for n in str(num)]
    n = len(nums)

    if len(nums) == 1:
        return -1
    elif len(nums) == 2:
        if nums[0] < nums[1]:
            return int(''.join([str(n) for n in nums[::-1]]))
        else:
            return -1

    # find out if list already in ascending order from the end - if so, next-bigger not possible
    # if there is a point when the ascending order breaks, then next-bigger is possible
    index = None
    for i in range(n - 1, 1, -1):
        if nums[i] > nums[i - 1]:
            index = i
            break
    if not index:
        # next-bigger not possible
        return -1

    # if next-bigger is possible, then swap element at index with the smallest number on RHS
    # - Find smallest in RHS
    smallest_index, smallest_value = None, sys.maxint
    for i in range(index, n):
        if nums[i] < smallest_value:
            smallest_value = nums[i]
            smallest_index = i
    # - Swap with smallest in RHS --> This will make the number Smaller
    nums[smallest_index], nums[index - 1] = nums[index - 1], nums[smallest_index]

    # sort all the elements to right of index, to ensure that this is the smallest number
    # --> This will ensure that the number is bigger, but the smallest
    nums = nums[0:index] + sorted(nums[index:n])

    # convert to number and return
    return int(''.join([str(n) for n in nums]))


## Q:: Given a sorted array with duplicates and a number, find the range in the form of (startIndex, endIndex) of that
#  number. For example,
# find_range({0 2 3 3 3 10 10},  3) should return (2,4).
# find_range({0 2 3 3 3 10 10},  6) should return (-1,-1).
# The array and the number of duplicates can be large.

def find_range(arr, n):
    from binary_search import binarySearch_First, binarySearch_Last
    return binarySearch_First(arr, n), binarySearch_Last(arr, n)


## Q:: You are given an unsorted array. Write an algorithm to extract the highest 'k' elements from the array.    
# Python Heap: https://docs.python.org/2/library/heapq.html

import heapq


def get_highest_elements(ip_list, k):
    # sorted(arr) --> returns a sorted list
    # arr.sort() --> sorts list in place

    n = len(ip_list)
    hlist = []  # to use as a heap

    # python only has a min heap implementation
    # to convert to a max heap, multiply by -1 when storing, and also multiply by -1 when retreiving

    for i in range(n):
        heapq.heappush(hlist, -1 * ip_list[i])

    return [-1 * heapq.heappop(hlist) for _ in range(k)]


## Q:: Given an array of elements, find the maximum possible sum of a contiguous subarray
# length -> min=1, max=n-1

def arr_max_sum_contiguous_elements(arr):
    n = len(arr)
    start = stop = 0
    sum = max_sum = 0

    for j in range(n):
        if sum == 0:
            start = j

        sum += arr[j]

        # if sum till then becomes less than zero, it will anyways not work, so break early
        if sum < 0:
            sum = 0

        elif sum > max_sum:
            stop = j
            max_sum = sum

    return max_sum, start, stop


## Q:: You are given an array of size 99. 98 elements are duplicate-pairs, leaving one that is unique.
# How would you find it?

def find_unique_element(arr):
    return reduce(lambda x, y: x ^ y, arr)
    # XOR of any value with itself is 0. 4^4 = 0    
    # XOR of 0 with any value is that value. 4^0 = 4


## Q:: You are given a list which represents Amazon's stock price each day. The values are the price of the Amazon
# stock. return the best profit that can be made from 1 purchase and 1 sale of Amazon stock.
# [2, 5, 4, 9, 1] --> Max profit is 7 by buying when the price is 2 and selling when the price is 9
# [2, 5, 4, 9, 1, 9] --> Max profit is 8 by buying when the price is 1 and selling when the price is 9
# [2, 1, 4, 10, 1, 9]

def max_profit(sp):
    """
    speed --> O(N)
    space --> O(1)
    """
    n = len(sp)
    minv = sp[0]
    max = 0
    tstart = start = stop = 0

    for i in range(n):
        if sp[i] < minv:
            minv = sp[i]
            tstart = i

        diff = sp[i] - minv
        if diff > max:
            max = diff
            start = tstart
            stop = i

    print 'range=({},{}), max={}'.format(start, stop, max)
    return max


## Q: Function to check if 2 strings are permutations of each other

def is_perm(s1, s2):
    d = dict()

    # if lengths are not equal, they cannot be permutations
    if not (len(s1) == len(s2)):
        return False
    else:
        # store all elements from s1 in the dict
        for s in s1:
            if d.get(s):
                d[s] += 1
            else:
                d[s] = 1

        # go through all elements in s2, and remove them from the dict as they are found            
        for s in s2:
            if d.get(s):
                if d[s] == 1:
                    del d[s]
                else:
                    d[s] -= 1
            else:
                return False

    return True if not d else False


# Q: Write a function that takes 2 input strings, and returns True if a permutation of the first string exists in
# the second string.

def perm_exists(s1, s2):
    """
    check if permutation of s1 exists in s2
    """
    d = dict()

    # store all elements of s2 in dict
    for s in s2:
        if not d.get(s):
            d[s] = 1
        else:
            d[s] += 1

    # check if all elements of s1 are in the dict
    for s in s1:
        if d.get(s):
            if d[s] == 1:
                del d[s]
            else:
                d[s] -= 1
        else:
            # element does not exist in dict
            return False

    return True

# Q. Function to check if a number is prime
def is_prime(num):
    if num < 4:
        return True

    for i in [2,3,5,7]:
        # if number is not prime, but is divisible by a prime number
        if num!=i and num%i == 0:
            return False
    return True


if __name__ == '__main__':

    for num in [2, 45, 1, 0, -32, 20, -20]:
        print 'num={}, twos={}'.format(num, calculate_two(num))

    arr = [2, 3, 4, 5, 6, 7]
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
    print 'no of paths with matrix {}x{} from ({},{}) to ({},{}) are {}'.format(m, n, start_x, start_y, stop_x, stop_y,
                                                                                unique_paths(stop_x=2, stop_y=6,
                                                                                             start_x=1, start_y=1, m=m,
                                                                                             n=n, visited_cells_orig=[
                                                                                        [None] * n for _ in range(m)]))

    print "-------------------------------------------------------"
    # permutations
    ip_word_list = ["AMOL", "AMI"]
    for ip_word in ip_word_list:
        generate_permutations(ip_list=ip_word, take_count=2)
        generate_combinations(ip_list=ip_word, take_count=2)

    print "-------------------------------------------------------"
    s = "molamol"
    print "first non repeating char in '{}' is '{}'. " \
          "find_first_non_repeating_char_2='{}'".format(s, find_first_non_repeating_char(s),
                                                        find_first_non_repeating_char_2(s))

    print "-------------------------------------------------------"
    ap_find_missing_element([1, 3, 5, 7, 9, 13, 15])

    print "-------------------------------------------------------"
    s = "abba"
    print 'largest subset palindrome in string {} is {}'.format(s, string_find_largest_subset_palindrome(s))

    print "-------------------------------------------------------"
    string_list = ["aaabbcccc",
                   "abbccasd",
                   "abbccdd"
                   ]
    for s in string_list:
        print 'compressed string for {} is {}'.format(s, compress_string(s))

    print "-------------------------------------------------------"
    main = "amolkokje"
    subs = ["amol", "aa", "kok", "molk", "amolkokje", "kje"]
    for s in subs:
        print '{} is substring of {} --> {}'.format(s, main, does_string_contain_substring(main, s))

    print "-------------------------------------------------------"
    num_list = [12, 513, 2017, 4132, 9, 111, 531]
    for num in num_list:
        print 'next closest bigger permutation of {} is {}'.format(num, next_bigger(num))

    print "-------------------------------------------------------"
    arr = [0, 2, 3, 3, 3, 10, 10]
    print 'arr={}, n={}, range={}'.format(arr, 3, find_range(arr, 3))
    print 'arr={}, n={}, range={}'.format(arr, 10, find_range(arr, 10))
    print 'arr={}, n={}, range={}'.format(arr, 6, find_range(arr, 6))
    print 'arr={}, n={}, range={}'.format(arr, 2, find_range(arr, 2))

    print "-------------------------------------------------------"
    arr = [4, 5, 6, 7, 2, 3, 1]
    k = 3
    print '{} highest elements of unsorted array {} --> {}'.format(k, arr, get_highest_elements(arr, k))

    print "-------------------------------------------------------"
    list_arr = [
        [2, -1, 2, 3, 4, -5],
        [2, -5, 2, 3, 4, -1],
        [2, 3, 4, 5, 6, 7],
        [2, 5, 7, 3, 2, 4],
        [4, 5, 7, 3, -2, 3]
    ]
    for arr in list_arr:
        print 'arr={}, max contiguous sum={}'.format(arr, arr_max_sum_contiguous_elements(arr))

    print "-------------------------------------------------------"
    arr = [4, 3, 2, 1, 4, 2, 1]
    print 'Unique element in {} is {}'.format(arr, find_unique_element(arr))

    print "-------------------------------------------------------"
    arrlist = [[2, 5, 4, 9, 1],
               [2, 5, 4, 9, 1, 9],
               [5, 3, 4, 12, 1, 9]
               ]
    for arr in arrlist:
        print 'max profit for {} is {}'.format(arr, max_profit(arr))

    print "-------------------------------------------------------"
    iplist = [('abc', 'cba'), ('abc', 'cbb')]
    for ip in iplist:
        print 's1={}, s2={}, is_perm={}'.format(ip[0], ip[1], is_perm(ip[0], ip[1]))

    print "-------------------------------------------------------"
    iplist = [['abc', 'bac'], ['abc', 'bacc'], ['abc', 'ab']]
    for ip in iplist:
        print 's1={}, s2={}, perm_exists={}'.format(ip[0], ip[1], perm_exists(ip[0], ip[1]))

    print "-------------------------------------------------------"
    num_list = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in num_list:
        print 'Num={}, Is Prime={}'.format(num, is_prime(num))
