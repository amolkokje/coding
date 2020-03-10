"""

Coding question:
Given a grid containing points that indicate heights at different points. Find the min-height of water required such
that it is not possible to reach from top-left to bottom-right.

FOLLOW-UP: Time complexity?
N - no of contour heights
m*n - grid size
O(N*m*n)

FOLLOW-UP: Heap time complexity?
O(logN) --> https://en.wikipedia.org/wiki/Binary_heap#Insert

HOW CAN YOU OPTIMIZE?
- Get a sorted height list
- Use binary-search approach to select heights to check for
"""
import heapq

grid = [
    [ 99, 2, 3, 4, 5, 6 ],
    [ 99, 2, 3, 4, 5, 6 ],
    [ 99, 2, 3, 4, 5, 6 ],
    [ 99, 2, 3, 4, 5, 6 ],
    [ 99, 2, 3, 4, 5, 6 ],
    [ 99, 2, 3, 4, 5, 99 ]
]

def get_min_height(grid):

    # get a sorted list of heights
    # option-1: add to heap and pull from there - O(logN)
    # option-2: add all to a list and sort the list - O(N*logN)
    height_heap = list()
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] not in height_heap:
                heapq.heappush(height_heap, grid[i][j])

    # check if path exists going from smallest to biggest
    while height_heap:
        curr_height = heapq.heappop(height_heap)
        if not path_exists(grid, m, n, curr_height):
            return curr_height

def path_exists(grid, m, n, curr_height):

    def _is_valid(px, py):
        return True if (px>=0 and px<m and py>=0 and py<n) else False

    visited = [ [False for _ in range(n)] for _ in range(m)]
    def _recurse(x, y):
        if visited[x][y] or grid[x][y]<curr_height:
            return False

        if x==m-1 and y==n-1:
            return True

        for nx,ny in [ (x+1,y), (x-1,y), (x,y+1), (x,y-1) ]:
            if _is_valid(nx,ny):
                visited[x][y] = True
                found = _recurse(nx, ny)
                visited[x][y] = False
                if found:
                    return found

    return _recurse(0,0)


