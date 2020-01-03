import sys, os, copy

############################################################
# binary search - sorted array
# works with repeating elements in the list

def binarySearch(input_list, x):
    """
    binary search on a sorted list
    None - when element not found
    index - when element found
    """
    left = 0
    right = len(input_list) - 1
    while left <= right:
        mid = (left + right) / 2
        if x > input_list[mid]:
            left = mid + 1
        elif x < input_list[mid]:
            right = mid - 1
        else:
            return mid
    return None


############################################################
# binary search recursive method - sorted array
# works with repeating elements in the
def binarySearchRecursive(x, left, right, ip_list):
    if left <= right:
        mid = (left + right) / 2
        if x > ip_list[mid]:
            return binarySearchRecursive(x, mid + 1, right, ip_list)
        elif x < ip_list[mid]:
            return binarySearchRecursive(x, left, mid - 1, ip_list)
        else:
            return mid


def binarySearchRecursive_helper(ip_list, x):
    return binarySearchRecursive(x, 0, len(ip_list) - 1, ip_list)


############################################################
# binary search last - sorted array
# e.g. [3,5,6,7,7,8]. Index of 7 is 4
# works with repeating elements in the list

def binarySearch_Last(ip_list, x):
    left = 0
    right = len(ip_list) - 1
    last = None
    while left <= right:
        mid = (left + right) / 2
        if x > ip_list[mid]:
            left = mid + 1
        elif x < ip_list[mid]:
            right = mid - 1
        else:
            last = mid
            left = mid + 1
    return last


############################################################
# binary search first - sorted array
# e.g. [3,5,6,7,7,8]. Index of 7 is 3
# works with repeating elements in the list

def binarySearch_First(ip_list, x):
    left = 0
    right = len(ip_list) - 1
    first = None
    while left <= right:
        mid = (left + right) / 2
        if x > ip_list[mid]:
            left = mid + 1
        elif x < ip_list[mid]:
            right = mid - 1
        else:
            first = mid
            right = mid - 1
    return first

############################################################
# Q: Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1. You may assume
# no duplicate exists in the array. Your algorithm's runtime complexity must be in the order of O(log n).
# Example 1: Input: nums = [4,5,6,7,0,1,2], target = 0 --> Output: 4
# Example 2: Input: nums = [4,5,6,7,0,1,2], target = 3 --> Output: -1

def binary_search_rotated_array(arr, x):
    n = len(arr)

    def _recurse(l, r):
        if l <= r:
            m = (l+r)/2
            if arr[m] == x:
                return m

            # if left side is not rotated
            #  - if element exists, go there, else go right
            if arr[l] <= arr[m]:
                if arr[l] <= x < arr[m]:
                    return _recurse(l, m-1)
                else:
                    return _recurse(m+1, r)

            # if right side is not rotated
            #  - if element exists, go there, else go left
            if arr[m] <= arr[r]:
                if arr[m] < x <= arr[r]:
                    return _recurse(m+1, r)
                else:
                    return _recurse(l, m-1)

    return _recurse(0, n-1)


############################################################
# binary search magic index - sorted array
# i.e. find index in sorted array such that ip_list[i]==i
# e.g. [-1,0,1,3,8,9]. Magic index is 3.
# NOTE: tests indicate that this algo goes in infinite loop when list has repeating elements. Example: [3,5,6,7,7,8]
# this can also be made non-recursive like the implementation of binarySearch()

# Book: 9.3
# Q. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
# FOLLOW UP: What if the values are not distinct?

def binary_search_magic_index_sorted_arr(arr):
    n = len(arr)

    def _recurse(l, r):
        if l <= r:
            m = (l + r) / 2
            if arr[m] == m:
                return m

            if m > arr[m]:
                return _recurse(m + 1, r)

            if m < arr[m]:
                return _recurse(l, m - 1)

    return _recurse(0, n - 1)


# NOTE: if given an array with no repeats, this will scale almost exactly like the previous method
def binary_search_magic_index_sorted_arr_with_repeats(arr):
    n = len(arr)

    def _recurse(l, r):
        if l <= r:
            m = (l + r) / 2
            if arr[m] == m:
                return m

            # search entire left side
            # left_max will be the new right to recurse on. For that we have 2 options:
            # 1. (m-1) --> same as general binary recursion case
            # 2. arr[m] --> this is the optimization. Since we are looking for MI, if there are repeats, we can shorten the search range
            left_max = min(m - 1, arr[m])
            left = _recurse(l, left_max)
            if left:
                return left

            right_min = max(m + 1, arr[m])
            right = _recurse(right_min, r)
            return right

    return _recurse(0, n - 1)


if __name__ == '__main__':

    # WORKS FOR: sorted arrays, repeats/non-repeats
    search_for = 5
    for iparr in [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3],
                  [5, 7, 8, 9, 4, 6],
                  [2, 3, 4, 5, 5, 8],
                  [8, 3, 4, 5, 5, 2]]:
        print 'IP: Arr={}, Search={}, Binary Search={}'.format(iparr, search_for, binarySearch(iparr, search_for))

    # WORKS FOR: sorted arrays, no-repeats
    print '----------------------------------------------------------'
    for iparr in [[-1, 0, 1, 3, 8, 9], [-4, -5, 0, 2, 4]]:
        print 'binary_search_magic_index_sorted_arr: ' \
              'IP={}, Magic Index={}'.format(iparr, binary_search_magic_index_sorted_arr(iparr))

    # WORKS FOR: sorted arrays, repeats/no-repeats
    print '----------------------------------------------------------'
    sorted_arr_repeats = [-10, -5, 2, 2, 2, 3, 4, 8, 9, 12, 13]
    print 'binary_search_magic_index_sorted_arr_with_repeats: ' \
          'IP={}, Magic Index with repeats={}'.format(sorted_arr_repeats,
                                                      binary_search_magic_index_sorted_arr_with_repeats(
                                                          sorted_arr_repeats))

    print '--------------------------------------------------------------'
    alist = [([4, 5, 6, 7, 0, 1, 2], 0), ([4, 5, 6, 7, 8, 1, 2, 3], 8)]
    for arr in alist:
        print 'binary_search_rotated_array: arr={}, target={}, output={}'.format(arr[0], arr[1],
                                                                                 binary_search_rotated_array(arr[0],
                                                                                                             arr[1]))
