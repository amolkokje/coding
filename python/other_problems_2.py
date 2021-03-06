import sys, os, copy, re


# Q: Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return
# the new length.

def removeDuplicates(arr):  # -> not sorted
    n = len(arr)
    i = 0
    eledict = dict()
    while i<n:
        if eledict.get(arr[i]):
            # go on until find an element at the end which is also not a duplicate
            while n>i and eledict.get(arr[n-1]):
                n -= 1

            # only if able to find an element before n<i, then swap
            if n-1>i:
                arr[i], arr[n-1] = arr[n-1], arr[i]
                n-=1
            else:
                break
        else:
            eledict[arr[i]] = 1
            i += 1

    del arr[n:]



def removeDuplicates2(arr):
    # NOTE: in absence of python set, put them in a dict with values as counts. Return only the dict.keys()
    # PYTHON-1 ---
    #return list(set(arr))

    # PYTHON-2 --- using a dictionary, and pop() -> also works for non-sorted lists
    """
    num_found_dict = dict()
    n = len(arr)
    i = 0

    while i < n:
        if num_found_dict.get(arr[i]):
            arr.pop(i)
            n -= 1
        else:
            num_found_dict[arr[i]] = 1
            i += 1
    """

    # NON-PYTHON --- Note: this trick only works for sorted arrays, but does not use pop()
    n = len(arr)
    if n == 0 or n == 1:
        return arr

    # stores index of arr for all unique elements
    j = 0

    # if there are no dups, i/j will increment together, else j will be behind i
    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1

    arr[j] = arr[n-1]
    j += 1
    del arr[j:]  # remove all elements at the end


# Q: Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and
# sell one share of the stock multiple times).

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
    nums[:] = nums[n - k:] + nums[:n - k]
    return nums


# Q: Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if
# every element is distinct.

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
    # xor = 0
    # for num in nums:
    #    xor ^= num
    # return xor

    # SOLUTION - 2 -- One liner, and same operation as before
    return reduce(lambda x, y: x ^ y, nums)


# Q: Given two arrays, write a function to compute their intersection. Each element in the result should appear as many
#  times as it shows in both arrays. The result can be in any order.
# Follow up:
#  ** What if the given array is already sorted? How would you optimize your algorithm?
#  ** What if nums1's size is small compared to nums2's size? Which algorithm is better?
#  ** What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements
# into the memory at once? --> HOW TO DO LAST PART?

def intersection(nums1, nums2):
    numd = dict()
    for l in nums1:
        if numd.get(l):
            numd[l] += 1
        else:
            numd[l] = 1

    intersection = list()
    for s in nums2:
        if numd.get(s):
            if numd[s] == 1:
                del numd[s]
            else:
                numd[s] -= 1
            intersection.append(s)

    return intersection


# Q: Given a non-empty array of digits representing a non-negative integer, plus one to the integer.


# The digits are stored such that the most significant digit is at the head of the list, and each element in the array
# contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
## NOTE: combining the array to create number may cause overflow if the number is very huge, if its some other language
#  like Java, etc. where the types are static
def plus_one(digits):
    # Optimization for this case
    if digits[-1] < 9:
        # simpler, since there will not be any carry
        digits[-1] += 1
        return digits
    else:
        # need complex operation as carry needs to be handled
        return add_numbers_using_arrs(digits, [1])


# Given 2 arrays representing numbers with MSB at head of list, give an output array containing their sum
def add_numbers_using_arrs(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    i1 = n1 - 1
    i2 = n2 - 1

    sum_arr = list()
    carry = 0

    while i1 >= 0 and i2 >= 0:
        temp_sum = arr1[i1] + arr2[i2] + carry
        if temp_sum >= 10:
            carry = 1
            val = int(str(temp_sum)[1])
        else:
            carry = 0
            val = temp_sum
        sum_arr.append(val)
        i1 -= 1
        i2 -= 1

    # only either or i1 or i2 will be >= 0
    while i1 >= 0:
        temp_sum = arr1[i1] + carry
        if temp_sum >= 10:
            carry = 1
            val = int(str(temp_sum)[1])
        else:
            carry = 0
            val = temp_sum
        sum_arr.append(val)
        i1 -= 1

    while i2 >= 0:
        temp_sum = arr2[i2] + carry
        if temp_sum >= 10:
            carry = 1
            val = int(str(temp_sum)[1])
        else:
            carry = 0
            val = temp_sum
        sum_arr.append(val)
        i2 -= 1

    if carry == 1:
        sum_arr.append(carry)

    return sum_arr[::-1]


# Q: Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
# the non-zero elements.

def move_zeros(arr):
    n = len(arr)
    i = 0
    while i<n:
        if arr[i] == 0:
            while arr[n-1] == 0:
                n -= 1
            if n-1 > i:
                arr[i], arr[n-1] = arr[n-1], arr[i]
            else:
                return
        i += 1
    #del arr[n:]   # use this if need to remove all the zeroes

    """
    while i < n:
        if nums[i] == 0:
            nums.append(nums.pop(i))
            n -= 1  # need to go till one less as the last one will be zero
        else:
            i += 1
    """

# Q: Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#  Each row must contain the digits 1-9 without repetition.
#  Each column must contain the digits 1-9 without repetition.
#  Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.  

def is_sudoku_valid(board):
    # board - 9x9 matrix, containing 9 boxes, each box containing 9 cells
    n = 9

    def contains_repeats(arr):
        # checks if thr list contains any repeats
        mod_arr = filter(lambda x: x != '.', arr)
        return False if len(set(mod_arr)) == len(mod_arr) else True

    # check rows and cols
    for i in range(n):
        if contains_repeats(board[i]) or contains_repeats([board[j][i] for j in range(n)]):
            return False

    # check 3x3 boxes        
    for i in range(0, n, 3):
        for j in range(0, n, 3):
            # convert box elements to arr
            if contains_repeats(board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]):
                return False

    return True


# Q: Given a string, find the length of the longest substring without repeating characters.

def length_longest_substring(s):
    def are_chars_repeating(s):
        return False if len(list(set(s))) == len(s) else True

    w = n = len(s)
    while w > 0:
        for i in range(n - w + 1):
            if not are_chars_repeating(s[i:i + w]):
                return s[i:i + w]
        w -= 1


        # Q: There are two sorted arrays nums1 and nums2 of size m and n respectively.


# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.    

def median_sorted_arrays(nums1, nums2):
    # 1 - merge the arrays, then sorte the merged array (method here) --> O(log(m+n))
    # 2 - create a new sorted array using method used in merge sort --> O(n)
    merged = sorted(nums1 + nums2)  # this part will take O(log (m+n))

    n = len(merged)
    mid = n / 2  # will default to int i.e. 7/2=3
    if n % 2 == 0:
        return float(merged[mid] + merged[mid + 1]) / 2
    else:
        return merged[mid]


# Q: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility);
# And then read line by line: "PAHNAPLSIIGYIR".
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

    mat = [[] for _ in range(num_rows)]
    current_row = 0
    for i in range(n):
        if current_row == 0 or current_row == (num_rows - 1):
            going_down = not going_down

        mat[current_row].append(s[i])

        if going_down:
            current_row += 1
        else:
            current_row -= 1

    return reduce(lambda x, y: x + y, mat)


# Q: Given a 32-bit signed integer, reverse digits of an integer.

def reverse_int(n):
    sn = str(n)
    if sn[0] == '-':
        return int(sn[0] + sn[:0:-1])
    else:
        return int(str(n)[::-1])


# Q: Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is
# found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
#  digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no
#  effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
# exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.   

def atoi(ints):
    def ret_value(n):
        n = int(n)
        if n > sys.maxint:
            return sys.maxint
        elif n < -sys.maxint:
            return -sys.maxint
        else:
            return n

    ints = ints.replace(' ', '')
    # print "**{}**".format(ints)
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
                if s[cs] != s[cs - 1]:
                    break
                cs += 1
            print '. END --> cs={}'.format(cs)

        elif p[cp] == '*':
            print '* START --> cp={}, cs={}'.format(cp, cs)
            while cs < ns:
                if s[cs] != s[cs - 1]:
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


# Suppose we have some input data describing a graph of relationships between parents and children over multiple
#  generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique
#  integer identifier.

# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:

# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   9


# Q:: Write a function that, for two given individuals in our dataset, returns true if and only if they share at
# least one ancestor.
# Sample input and output:
# parentChildPairs, 3, 8 => false
# parentChildPairs, 5, 8 => true
# parentChildPairs, 6, 8 => true
# pair = (parent, child)

# NOTE - Solution can be made faster with memoization on the _recurse() method

# Solution without any node data struct
# BFS
def have_common_ancestors_BFS(pairs, n1, n2):
    def _get_ancestors(child):
        queue = list()
        ancestors = list()

        # add the child of interest to queue
        for p in pairs:
            if p[1] == child:
                queue.append(p[0])
                ancestors.append(p[0])

        while queue:
            p = queue.pop(0)

            # find all the parents, and add to queue
            for pair in pairs:
                if pair[1] == p:
                    queue.append(pair[0])
                    ancestors.append(pair[0])
                    # print 'q={}, a={}'.format(queue, ancestors)

        return ancestors

    anc_n1 = _get_ancestors(n1)
    anc_n2 = _get_ancestors(n2)
    # print anc_n1, anc_n2
    common_anc = filter(lambda x: x in anc_n2, anc_n1)
    return True if common_anc else False


# DFS
def have_common_ancestors_DFS(pairs, n1, n2):
    def _get_parent_names(child_node_name):
        parent_names = list()
        for pair in pairs:
            if pair[1] == child_node_name:
                parent_names.append(pair[0])
        return parent_names

    def _get_ancestors(child_node_name):
        ancestors = list()

        def _recurse(child_node_name):
            parent_names = _get_parent_names(child_node_name)
            if parent_names:
                ancestors.extend(parent_names)
                for parent_name in parent_names:
                    _recurse(parent_name)

        _recurse(child_node_name)
        return ancestors

    anc_n1 = _get_ancestors(n1)
    anc_n2 = _get_ancestors(n2)
    # print anc_n1, anc_n2
    common_anc = filter(lambda x: x in anc_n2, anc_n1)
    return True if common_anc else False


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

    output = [[], []]
    for node, parent_count in node_parents.iteritems():
        if parent_count == 0:
            output[0].append(node)
        elif parent_count == 1:
            output[1].append(node)

    return output


# Q: Given an unsorted integer array, find the smallest missing positive integer.
def first_missing_positive(nums):
    # linear method that will be acceptable to all, add all elments to min heap
    i = 1
    while True:
        if i not in nums:
            return i
        else:
            i += 1


def replace_spaces_in_str(arr, replace_by='%20'):
    n = len(arr)
    i = 0

    replace_by_arr = [c for c in replace_by]
    m = len(replace_by_arr)

    def replace_and_shift(index):
        # increase the size of input array by length of shift char
        arr.extend([None for _ in range(m)])
        # shift right
        arr[index + m:n + m] = arr[index + 1:n]
        # add
        arr[index:index + m] = replace_by_arr

    while i < n:
        if arr[i] == ' ':
            replace_and_shift(i)
            n += m - 1
            i += m
        else:
            i += 1
    return arr


# Book: 1.6
# Q. Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate
# the image by 90 degrees. Canyou do this in place?

def rotate_image_matrix_by_90(matrix):
    n = len(matrix)  # will always be even for NxN matrix
    layer_count = n / 2

    for layer in range(layer_count):
        # for 5x5, L=5/2=2 --> L=0:(0:n), L=1:(1:n-1), L=2:(2:n-2)
        swap_range = range(0 + layer, n - layer)
        # print 'Layer:{}, Range:{}'.format(layer, swap_range)

        # top in temp
        temp = [matrix[layer][r] for r in swap_range]

        # print 'top=right'
        for r in swap_range[::-1]:  ## NOTE: reverse to avoid overwrite before shift
            matrix[layer][r] = matrix[r][n - layer - 1]
        # print matrix

        # print 'right=bottom'
        for r in swap_range[::-1]:
            matrix[r][n - layer - 1] = matrix[n - layer - 1][r]
        # print matrix

        # print 'bottom=left'
        for r in swap_range[::-1]:
            matrix[n - layer - 1][r] = matrix[r][layer]
        # print matrix

        # print 'left=top'
        for r in swap_range[::-1]:
            matrix[r][layer] = temp[r]


# Book: 3.6
# Q. Write a program to sort a stack in ascending order (with biggest items on top). You may use at most one additional
#  stack to hold items, but you may not copy the elements into any other data structure (such as an array). The stack
# supports the following operations: push, pop, peek, and isEmpty.
from fb_samples import Stack


def sort_stack_using_additional_stack(input_stack):
    new_stack = Stack()

    # add an element in the new stack to start with
    new_stack.insert(input_stack.get())

    # add elements in sorted order to new stack. This should be reverse sorted of the required order
    while not input_stack.is_empty():
        temp = input_stack.get()
        c = 0
        # until the element is smaller than the seen value, remove elements from new stack and place in input stack
        while temp > new_stack.check() and not new_stack.is_empty():
            input_stack.insert(new_stack.get())
            c += 1  # maintain count of how many elements moved, so they can be put back in the new stack
        new_stack.insert(temp)

        # put all the removed elements back in the new stack
        for _ in range(c):
            new_stack.insert(input_stack.get())

    # move all elements back
    while not new_stack.is_empty():
        input_stack.insert(new_stack.get())


# Book: 9.6
# Q. Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n-pairs of
# parentheses.

def get_all_valid_parentheses(count):
    valid = list()

    def _recurse(formed, open, closed):
        if open==0 and closed==0:
            valid.append(formed)
            return

        if open==closed:
            if open>=0:
                _recurse(formed+'(', open-1, closed)
        elif open<closed:
            if open>=0:
                _recurse(formed+'(', open-1, closed)
            if closed>=0:
                _recurse(formed+')', open, closed-1)

    _recurse('', count, count)
    return valid

# Book: 9.8
# Q. Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write
# code to calculate the number of ways of representing n cents.
# NOTE: can use memoization

def ways_to_represent_n_cents(n):
    def _recurse(x):
        if x < 0:
            return 0

        elif x == 0:
            return 1

        else:
            count_ways = 0
            for cent in [25, 10, 5, 1]:
                count_ways += _recurse(x - cent)
            return count_ways

    return _recurse(n)


# Book: 11.1
# Q. You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order

def merge_sorted_arr(a, b):
    na = len(a)
    nb = len(b)

    # buffer in a for b
    a += [None for _ in range(nb)]

    ia = 0
    ib = 0
    while ia < na and ib < nb:
        # if found, then add in a, and shift a to the right
        if b[ib] <= a[ia]:
            a[ia + 1:na + 1] = a[ia:na]
            a[ia] = b[ib]
            na += 1
            ib += 1
        else:
            # else, check next element of a
            ia += 1

    # if any bigger elements still present in b
    while ib < nb:
        a[ia] = b[ib]
        na += 1
        ia += 1
        ib += 1


# Book: 11.5
# Q. Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of
# a given string.
# Simplify: replace string by chars
# Approach: use binary search, and if empty string is found, move to closest non-empty string and keep going

def find_str_from_sorted_arr_of_empty_and_nonempty_strings(arr, x):
    def _recurse(l, r):
        if l <= r:
            m = (l + r) / 2
            if arr[m] == x:
                return m

            if arr[m] == '':
                # find closest non-empty str
                # left_closest = m - 1
                # right_closest = m + 1

                move = 1

                # in each loop iteration, keep going-left, and going-right. Stop when you find a value.
                while True:
                    left_closest = m - move
                    if left_closest > 0 and arr[left_closest] != '':
                        m = left_closest
                        break
                    right_closest = m + move
                    if right_closest < n and arr[right_closest] != '':
                        m = right_closest
                        break
                    move += 1

                if arr[m] == x:
                    return m
                elif arr[m] > x:
                    return _recurse(l, m - 1)
                else:
                    return _recurse(m + 1, r)

            if arr[m] > x:
                return _recurse(l, m - 1)
            else:
                return _recurse(m + 1, r)

    return _recurse(0, len(arr) - 1)




if __name__ == '__main__':

    print '--------------------------------------------------------------'
    arrlist = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4]]
    for arr in arrlist:
        print 'BEFORE: arr={}'.format(arr)
        removeDuplicates(arr)
        print 'AFTER REMOVING DUPLICATES: arr={}'.format(arr)

    print '--------------------------------------------------------------'
    arrlist = [[7, 1, 5, 3, 6, 4], [1, 2, 3, 4, 5], [7, 6, 4, 3, 1]]
    for arr in arrlist:
        print 'prices={}, max_profit={}'.format(arr, max_profit(arr))

    print '--------------------------------------------------------------'
    arrlist = [([1, 2, 3, 4, 5, 6, 7], 3), ([-1, -100, 3, 99], 2), (range(20), 2)]
    for arr in arrlist:
        print 'arr={}, k={}'.format(arr[0], arr[1])
        print 'rotated={}'.format(rotate_array(arr[0], arr[1]))

    print '--------------------------------------------------------------'
    arrlist = [[1, 2, 3, 1], [1, 2, 3, 4, 5], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]
    for arr in arrlist:
        print 'arr={}, contains_duplicates={}'.format(arr, contains_duplicates(arr))

    print '--------------------------------------------------------------'
    arrlist = [[2, 1, 2], [4, 1, 2, 2, 1]]
    for arr in arrlist:
        print 'arr={}, single_number={}'.format(arr, single_number(arr))

    print '--------------------------------------------------------------'
    for nums in [([1, 2, 2, 1], [2, 2]),
                 ([4, 9, 5], [9, 4, 9, 8, 4])
                 ]:
        print 'nums1={}, nums2={}, intersection={}'.format(nums[0], nums[1], intersection(nums[0], nums[1]))

    print '--------------------------------------------------------------'
    arrlist = [[1, 2, 3], [4, 3, 2, 1], [1, 9], [1, 0], [9, 9, 9, 9], [1, 9, 9, 9]]
    for arr in arrlist:
        print 'digits={}'.format(arr)
        # cannot print both in same line as list is mutable and so it updates in place
        print '--> add_numbers_using_arrs={}'.format(add_numbers_using_arrs(arr, arr))
        print '--> plus_one={}'.format(plus_one(arr))

    print '--------------------------------------------------------------'
    arrlist = [[0, 1, 0, 3, 12], [0, 1, 0, 0, 0, 0, 3, 12]]
    for arr in arrlist:
        print 'arr={}'.format(arr)
        move_zeros(arr)
        print '-- move_zeros={}'.format(arr)

    print '--------------------------------------------------------------'
    board_list = [
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ],
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
    ]
    for board in board_list:
        print 'is_sudoku_valid={}'.format(is_sudoku_valid(board))
    sys.exit()

    print '--------------------------------------------------------------'
    arrlist = ["abcabcbb", "bbbbb", "pwwkew"]
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
    arrlist = [("PAYPALISHIRING", 3), ("PAYPALISHIRING", 4)]
    for arr in arrlist:
        print ''.join(convert(arr[0], arr[1]))

    print '--------------------------------------------------------------'
    nlist = [123, -123, 120]
    for n in nlist:
        print 'n={}, reverse={}'.format(n, reverse_int(n))

    print '--------------------------------------------------------------'
    nlist = ["42", "   -42", "4193 with words", "words and 987", "-91283472332"]
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
    pairs = [(3, 8), (5, 8), (6, 8)]
    for pair in pairs:
        print '{} and {}: hcaDFS={}, hcaBFS={}'.format(pair[0], pair[1],
                                                       have_common_ancestors_BFS(parent_child_pairs, pair[0], pair[1]),
                                                       have_common_ancestors_DFS(parent_child_pairs, pair[0], pair[1]))

    print '--------------------------------------------------------------'
    alist = [[1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12]]
    for arr in alist:
        print 'first_missing_positive input={}, output={}'.format(arr, first_missing_positive(arr))

    print '--------------------------------------------------------------'
    iplist = ['Amol is Best']
    for ip in iplist:
        ip_arr = [c for c in ip]
        print 'replace_spaces_in_str input={}'.format(ip_arr)
        replace_spaces_in_str(ip_arr)
        print 'output={}'.format(ip_arr)

    print '--------------------------------------------------------------'
    ip_matrix = [['a', 'b', 'c'] for _ in range(3)]
    print 'input matrix={}'.format(ip_matrix)
    rotate_image_matrix_by_90(ip_matrix)
    print 'output={}'.format(ip_matrix)

    """
    print '--------------------------------------------------------------'
    ipstack = Stack()
    for value in [1, 3, 8, 12, 5, 10, 7]:
        ipstack.insert(value)
    print 'Input Stack: {}'.format(ipstack)
    sort_stack_using_additional_stack(ipstack)
    print '      Sorted using additional stack: {}'.format(ipstack)
    """

    print '--------------------------------------------------------------'
    for count in [2, 3]:
        print 'Count={}, Valid Parentheses String List={}'.format(count, get_all_valid_parentheses(count))
    
    print '--------------------------------------------------------------'
    for cents in [10,
                  # 50
                  ]:
        print 'Cents={}, Ways to represent={}'.format(cents, ways_to_represent_n_cents(cents))

    for arrs in [(range(3), range(5))]:
        print 'Arrs={}'.format(arrs)
        merge_sorted_arr(arrs[0], arrs[1])
        print '-- After Merging: Arrs={}'.format(arrs)

    print '--------------------------------------------------------------'
    for iparr in [[1, 2, '', '', '', '', 3, '', '', 4, 5, '', 6, 7, 8, 9]]:
        print 'arr={}'.format(iparr)
        for find in [2, 3, 8]:
            print 'find={}, ' \
                  'find_str_from_sorted_arr_of_empty_and_nonempty_strings={}'.format(find,
                                                                                     find_str_from_sorted_arr_of_empty_and_nonempty_strings(
                                                                                         iparr, find))
