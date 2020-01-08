
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

        div = max(nums)   # TODO - this can be improved
        div_result_dict = dict()

        while div >= 1:
            result = 0
            #print 'div={}'.format(div)
            for n in nums:
                result += int(math.ceil(float(n)/float(div)))
            div_result_dict[div] = result
            div -= 1
        print div_result_dict

        smallest_div = None
        #closest_val = -99
        smallest_gap = None
        biggest_found = -1
        ret = -1
        for div, result in div_result_dict.iteritems():
            if result <= threshold and result > biggest_found:
                biggest_found = result
                ret = div
                #print 'd={}, r={}, ret={}, biggest={}'.format(div, result, ret, biggest_found)
        return ret






"""
https://leetcode.com/contest/weekly-contest-166/problems/group-the-people-given-the-group-size-they-belong-to/
"""

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        n = len(groupSizes) # total number of people

        group_sizes = list(set(groupSizes))
        groups_by_size = list()

        for group_size in group_sizes:
            all_groups_of_given_size = list()
            # get array indices
            for i in range(len(groupSizes)):
                if groupSizes[i] == group_size:
                    all_groups_of_given_size.append(i)

            #print 'size={}, groups={}'.format(group_size, all_groups_of_given_size)
            total_groups = len(all_groups_of_given_size)/group_size
            groups_list = list()
            for k in range(total_groups):
                #print 'k={}, start={}, stop={}'.format(k, k*group_size, k*group_size+group_size)
                groups_list.append(all_groups_of_given_size[k*group_size:k*group_size+group_size])
            #print 'groups_list={}'.format(groups_list)
            groups_by_size.extend(groups_list)

        return groups_by_size
        # print gp_pairs




"""
https://leetcode.com/contest/weekly-contest-166/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [ int(s) for s in str(n) ]
        p = 1
        s = 0

        for i in range(len(nums)):
            p *= nums[i]
            s += nums[i]
        return p-s

