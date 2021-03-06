import sys, os, copy


# Q. Given a string, find the length of the longest substring without repeating characters.
# FASTEST: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/452615/Python-100-or-easy-Explanation-with-VIDEO-and-CODE

def lengthOfLongestSubstring(s):
    def _has_repeats(s):
        # print 'check: {}'.format(s)
        return False if len(s) == len(set(s)) else True

    n = len(s)

    if n == 0:
        return 0

    str_len = n
    while str_len > 0:
        start_pts = range(n - str_len + 1)
        for start_pt in start_pts:
            if not _has_repeats(s[start_pt:start_pt + str_len]):
                return str_len
        str_len -= 1

    return 0


# TODO: Try to do all in a single iteration

# Q. Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

def get_two_sum(arr, target):
    arr_dict = dict()
    n = len(arr)
    output_set = set()

    for i in range(n):
        if arr_dict.get(target - arr[i]):
            # NOTE: it is important to note here that sorted elements are added to avoid all the if-conditions
            output_set.add(tuple(sorted([arr[i], target - arr[i]])))
        arr_dict[arr[i]] = target - arr[i]

    return list(output_set)


# NOTE: list() cannot be added to set() as list() is mutable and set() is immutable. So have to add tuple()
def get_num_sum(arr, target, count):
    n = len(arr)
    three_sum_set = set()
    visited = [False for _ in range(n)]
    num_list = list()

    def _recurse(i):
        if visited[i]:
            return

        if len(num_list) > (count - 1):
            return

        if len(num_list) == count - 1:
            if sum(num_list) + arr[i] == target:
                # converting to tuple and adding to set will ensure there are no duplicates
                three_sum_set.add(tuple(sorted(num_list + [arr[i]])))
                return

        for k in range(i + 1, n):
            visited[i] = True
            num_list.append(arr[i])
            _recurse(k)
            visited[i] = False
            num_list.pop(-1)

    for i in range(n):
        _recurse(i)

    return three_sum_set


#############################


# Q. Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
#  represent. A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not
# map to any letters.
# Example: INPUT: "23" OUTPUT: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note: Although the above answer is in lexicographical order, your answer could be in any order you want.
# REF: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Unable to compare solution with LeetCode since the output there is in order

number_letter_dict = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l']
}


def generate_combinations(nums):
    n = len(nums)
    out = list()
    nums = map(int, nums)

    def _recurse(numi, formed):
        if numi == n:
            out.append(formed)
            return

        for letter in number_letter_dict[nums[numi]]:
            _recurse(numi+1, formed+letter)

    _recurse(0, '')
    return out

# Q. Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Example 1: Input: "()" Output: true
# Example 2: Input: "()[]{}" Output: true
# Example 3: Input: "(]" Output: false
# Example 4: Input: "([)]" Output: false
# Example 5: Input: "{[]}" Output: true
# REF: https://leetcode.com/problems/valid-parentheses/submissions/

def is_bracket_string_valid(s):
    closed_matches = {')': '(', ']': '[', '}': '{'}
    closed_brackets = closed_matches.keys()
    open_brackets = ['(', '[', '{']
    stack = list()

    for i in s:
        if i in open_brackets:
            stack.append(i)

        elif i in closed_brackets:
            if len(stack) > 0:  # if no opening bracket found in the beginning
                if stack[-1] == closed_matches[i]:
                    stack.pop(-1)
                else:
                    return 'NO'
            else:
                return 'NO'  # invalid bracket found

        else:
            return 'NO'

    # if not enough closing brackets found
    if len(stack) > 0:
        return 'NO'

    return 'YES'


if __name__ == '__main__':

    iplist = ['', 'pwwkew', 'abcabcbb']
    for ip in iplist:
        print 'ip={}, output={}'.format(ip, lengthOfLongestSubstring(ip))

    print '**************************'
    ### NOTE--> Solution does not work for [0,0,0]
    iplist = [{'arr': [0, 2, 3, 4, 5], 'target2': 5, 'target3': 5},
              {'arr': [1, 2, 0, 4, 5], 'target2': 6, 'target3': 6},
              {'arr': [-1, 0, 1, 2, -1, -4], 'target2': 6, 'target3': 0},
              ]
    for ip in iplist:
        print 'target2={}, target3={}, arr={}'.format(ip['target2'], ip['target3'], ip['arr'])
        print 'output2={}, output3={}'.format(get_two_sum(ip['arr'], ip['target2']),
                                              get_num_sum(ip['arr'], ip['target3'], 3))

    print '**************************'
    nums_list = ["23",
                 "2345",
                 "234"
                 ]
    for nums in nums_list:
        print '----------------'
        print 'nums={}, letter combinations={}'.format(nums, generate_combinations(nums))

    print '**************************'
    str_list = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for s in str_list:
        print 'str={}, is_valid={}'.format(s, is_bracket_string_valid(s))