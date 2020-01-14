import copy

"""
https://leetcode.com/contest/weekly-contest-162/problems/number-of-closed-islands/
"""
# UNDERSTAND WELL - SEE

class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)  # rows
        n = len(grid[0])  # cols

        ## test a coordinate is valid (not out of grid)
        def _is_valid(p):
            if p[0]>=0 and p[1]>=0 and p[0]<m and p[1]<n:
                return True
            return False

        res = 0

        ## loop through all coordinates
        for r in range(m):
            for c in range(n):
                print r,c

                ## if current point island
                if grid[r][c] == 0:
                    ## dsf --> 1: turn land to water to not revisit; 2: test the current land is closed
                    is_closed = True
                    queue = [(r,c)]
                    while queue:
                        x, y = queue.pop(0)

                        if grid[x][y] == 0:
                            ## turn land to water
                            grid[x][y] = 1

                            ## get all next coordinates in four directions, and filter out the points out of grid
                            valid_next = [p for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if _is_valid(p)]

                            ## once any valid points are out of grid (not closed)
                            ## is_closed will accumulate to False
                            is_closed &= len(valid_next) == 4
                            print is_closed

                            #if not is_closed:
                            #    break

                            ## continue with dsf
                            queue += valid_next

                    if is_closed:
                        res += 1
                        #res += int(is_closed)

        return res

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
        m = len(colsum)  # cols
        #n = 2 # rows
        bupper = upper
        blower = lower

        mat = [ [0 for _ in range(m)] for _ in range(2) ]

        invalid = False
        for i in range(m):
            if colsum[i] == 2:
                if upper==0 or lower==0:
                    invalid=True
                    break

                mat[0][i] = 1
                mat[1][i] = 1
                upper -= 1
                lower -= 1

            elif colsum[i] == 1:
                if upper==0 and lower==0:
                    invalid=True
                    break

                if upper >= lower:
                    mat[0][i] = 1
                    upper -=1
                else:
                    mat[1][i] = 1
                    lower -=1


            elif colsum[i] == 0:
                mat[0][i] = 0
                mat[1][i] = 0

        print mat
        print sum(mat[0]), bupper
        print sum(mat[1]), blower
        if sum(mat[0])!=bupper or sum(mat[1])!=blower:
            invalid = True

        if invalid:
            return []

        return mat


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
        #print mat

        for x, count in x_dict.iteritems():
            #print 'x={}, count={}'.format(x, count)
            mat[x] = [ mat[x][k]+count for k in range(m) ]
            #print '*',mat
        print mat

        for y, count in y_dict.iteritems():
            #print 'y={}, count={}'.format(y, count)
            for r in range(n):
                mat[r][y] += count
        print mat

        odds = 0
        for r in range(n):
            odds += len(filter(lambda x:x%2!=0, mat[r]))
        return odds




