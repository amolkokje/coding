import os, sys, copy

"""
https://leetcode.com/contest/weekly-contest-162/problems/reconstruct-a-2-row-binary-matrix/
"""


class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n = len(colsum)
        upper_sum = 0
        lower_sum = 0
        output = [ list(), list() ]
        for i in range(n):

            if colsum[i] == 2:
                if upper_sum == upper or lower_sum == lower:
                    return []
                output[0].append(1)
                output[1].append(1)
                upper_sum += 1
                lower_sum += 1

            elif colsum[i] == 1:

                if upper_sum == upper and lower_sum == lower:
                    return []
                if upper_sum < upper or lower_sum < lower:
                    if (upper-upper_sum) >= (lower-lower_sum):
                        output[0].append(1)
                        output[1].append(0)
                        upper_sum += 1
                    else:
                        output[0].append(0)
                        output[1].append(1)
                        lower_sum += 1

            elif colsum[i] == 0:
                output[0].append(0)
                output[1].append(0)

        if len(output[0]) < n or upper_sum!=upper or lower_sum!=lower:
            return []
        return output

"""
https://leetcode.com/contest/weekly-contest-162/problems/cells-with-odd-values-in-a-matrix/
"""

class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        # reverse: n-rows, m-cols

        x_dict = dict()
        y_dict = dict()

        # get count of rows/cols that need to be updated
        for index in indices:
            if not x_dict.get(index[0]):
                x_dict[index[0]] = 1
            else:
                x_dict[index[0]] += 1

            if not y_dict.get(index[1]):
                y_dict[index[1]] = 1
            else:
                y_dict[index[1]] += 1

        mat = [ [0 for _ in range(m)] for _ in range(n) ]

        # update the matrix
        for i in range(n):
            for j in range(m):
                if x_dict.get(i):
                    mat[i][j] += x_dict[i]
                if y_dict.get(j):
                    mat[i][j] += y_dict[j]

        # calculate odd values
        odds = 0
        for r in range(n):
            odds += len(filter(lambda x:x%2!=0, mat[r]))
        return odds



"""
https://leetcode.com/contest/weekly-contest-162/problems/number-of-closed-islands/
"""

# AMOL - Good one
def get_island_count(grid):
    m = len(grid)  # rows
    n = len(grid[0])  # cols
    print m, n

    def _is_valid(point):
        if point[0] >= 0 and point[1] >= 0 and point[0] < m and point[1] < n:
            return True
        return False

    # LOGIC:
    # Find a point that is land-0, and check if it has valid pts around it, which will indicate its not in a corner
    # Then find all the connected land-0 points for that point. If all the connected land-0 points are valid, then its an island
    # Iterate ---
    # As you go through the land points, flip them to water so we dont get back to them


    island_count = 0

    for i in range(m):
        for j in range(n):

            if grid[i][j] == 0:
                queue = [(i, j)]
                is_closed = True

                while queue:
                    x, y = queue.pop(0)

                    grid[x][y] = 1

                    valid_pts = list()
                    for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if _is_valid(p):
                            valid_pts.append(p)

                    # this means that reached a corner, and hence this island is not valid
                    if not len(valid_pts) == 4:
                        is_closed = False

                    # island or not, go ahead and visit all the points and mark them, so they are not
                    # visited again in the next iteration
                    for p in valid_pts:
                        if grid[p[0]][p[1]] == 0:
                            queue.append(p)
                            # raw_input(queue)

                if is_closed:
                    island_count += 1

    return island_count


if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    print grid
    print 'ISLANDS={}'.format(get_island_count(grid))

    grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
    print grid
    print 'ISLANDS={}'.format(get_island_count(grid))


    grid = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]]
    print grid
    print 'ISLANDS={}'.format(get_island_count(grid))
