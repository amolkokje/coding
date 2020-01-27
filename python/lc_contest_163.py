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

        # convert to a list
        grid_list = list()
        for i in range(m):
            grid_list += grid[i]

        # shift it
        total = m * n
        if k > total:
            k = k % total
        grid_list = grid_list[total - k:] + grid_list[:total - k]

        # convert to a grid
        for i in range(m):
            grid[i] = grid_list[(i * n):(i * n) + n]

        return grid


"""
https://leetcode.com/contest/weekly-contest-163/problems/greatest-sum-divisible-by-three/
"""


class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        visited = [False for _ in range(n)]
        max_sum = 0

        def _recurse(i, curr_sum, max_sum):
            if visited[i]:
                return

            curr_sum += nums[i]
            if curr_sum % 3 == 0:
                if curr_sum > max_sum:
                    max_sum = curr_sum

            for k in range(i + 1, n):  # combinations, no need to test all permutations
                visited[i] = True
                found_sum = _recurse(k, curr_sum, max_sum)
                if found_sum and found_sum > max_sum:
                    max_sum = found_sum
                visited[i] = False

            return max_sum

        for i in range(n):
            found_sum = _recurse(i, 0, max_sum)
            if found_sum and found_sum > max_sum:
                max_sum = found_sum

        return max_sum
