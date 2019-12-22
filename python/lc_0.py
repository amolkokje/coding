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


# Q. Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.'

def get_two_sum(arr, target, skip_index=None):
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
def get_three_sum(arr, target):
    three_sum_set = set()
    n = len(arr)
    for i in range(n):
        two_sum_list = get_two_sum(arr, target - arr[i])
        if two_sum_list:
            # convert all to tuple() from the list to list()
            two_sum_list = [list(t) for t in two_sum_list]

            for two_sum in two_sum_list:  # ASSUMPTION: all non-repeating numbers in the list
                if not arr[i] in two_sum:
                    two_sum.append(arr[i])
                    three_sum_set.add(tuple(sorted(two_sum)))

    return list(three_sum_set)


if __name__ == '__main__':

    iplist = ['', 'pwwkew', 'abcabcbb']
    for ip in iplist:
        print 'ip={}, output={}'.format(ip, lengthOfLongestSubstring(ip))

    print '**************************'
    ### NOTE--> Solution does not work for [0,0,0]
    iplist = [{'arr': [0, 2, 3, 4, 5], 'target2': 5, 'target3': 5},
              {'arr': [1, 2, 0, 4, 5], 'target2': 6, 'target3': 6},
              {'arr': [-1,0,1,2,-1,-4], 'target2': 6, 'target3': 0},
              ]
    for ip in iplist:
        # print ip
        print 'arr={}, output2={}, output3={}'.format(ip['arr'], get_two_sum(ip['arr'], ip['target2']),
                                                      get_three_sum(ip['arr'], ip['target3']))
        # rint 'arr={}, output={}'.format(ip['arr'], get_two_sum(ip['arr'], ip['target']))
