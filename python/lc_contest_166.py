"""
https://leetcode.com/contest/weekly-contest-166/problems/find-the-smallest-divisor-given-a-threshold/
"""

import math


class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        div = 1
        while True:
            # NOTE: convert the numerator to float first, to get the output as float, or else it will be an int by default
            result = sum([math.ceil(float(n) / div) for n in nums])
            print 'div={}, result={}'.format(div, result)
            if result < threshold:
                return int(result)
            div += 1


"""
https://leetcode.com/contest/weekly-contest-166/problems/group-the-people-given-the-group-size-they-belong-to/
"""


## SOLUTION - 1
class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        n = len(groupSizes)  # total number of people

        group_sizes = list(set(groupSizes))
        groups_by_size = list()

        for group_size in group_sizes:
            all_groups_of_given_size = list()
            # get array indices
            for i in range(len(groupSizes)):
                if groupSizes[i] == group_size:
                    all_groups_of_given_size.append(i)

            # print 'size={}, groups={}'.format(group_size, all_groups_of_given_size)
            total_groups = len(all_groups_of_given_size) / group_size
            groups_list = list()
            for k in range(total_groups):
                # print 'k={}, start={}, stop={}'.format(k, k*group_size, k*group_size+group_size)
                groups_list.append(all_groups_of_given_size[k * group_size:k * group_size + group_size])
            # print 'groups_list={}'.format(groups_list)
            groups_by_size.extend(groups_list)

        return groups_by_size
        # print gp_pairs


## SOLUTION - 2
class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """

        group_dict = dict()
        n = len(groupSizes)
        i = 0
        while i < n:
            if group_dict.get(groupSizes[i]):
                group_dict[groupSizes[i]].append(i)
            else:
                group_dict[groupSizes[i]] = [i]
            i += 1

        # massage group dict to split per max size
        group_lists = list()
        for k, v in group_dict.iteritems():
            list_len = len(v)
            # print 'k={}, v={}, len={}'.format(k,v,list_len)
            if list_len == k:
                group_lists.append(v)
            elif list_len > k:
                list_count = list_len / k
                # print 'list_count={}'.format(list_count)
                for t in range(list_count):
                    group_lists.append(v[(t * k):(t * k) + k])

        return group_lists


"""
https://leetcode.com/contest/weekly-contest-166/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""


class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [int(s) for s in str(n)]
        p = 1
        s = 0

        for i in range(len(nums)):
            p *= nums[i]
            s += nums[i]
        return p - s
