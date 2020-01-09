"""
https://leetcode.com/contest/weekly-contest-163/problems/shift-2d-grid/
"""

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)  # rows
        n = len(grid[0])  # cols
        #print 'm={}, n={}'.format(m,n)
        #print grid[0]

        # convert to a list
        grid_list = list()
        for i in range(m):
            grid_list.extend(grid[i])
        #print grid_list

        # shift it
        total = m*n
        if k > total:
            k = k%total

        grid_list = grid_list[total-k:] + grid_list[:total-k]
        #print grid_list

        # convert to a grid
        k = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = grid_list[k]
                k += 1

        return grid


"""
https://leetcode.com/contest/weekly-contest-163/problems/greatest-sum-divisible-by-three/
"""

import copy

class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        visited = [ False for _ in range(n) ]
        sum_list = list()

        def _recurse(visited, i, curr_sum):
            if visited[i]:
                return

            curr_sum += nums[i]
            if curr_sum%3 == 0:
                sum_list.append(curr_sum)

            visited_local = copy.deepcopy(visited)

            for k in range(i+1, n):
                _recurse(visited_local, k, curr_sum)

        for i in range(n):
            _recurse(visited, i, 0)

        #print sum_list
        if sum_list:
            return max(sum_list)
        else:
            return 0

        