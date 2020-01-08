
"""
https://leetcode.com/contest/weekly-contest-167/problems/shortest-path-in-a-grid-with-obstacles-elimination/
"""
import copy

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)  #y -> columns
        n = len(grid[0])  #x -> rows
        #print 'm={}, n={}'.format(m, n)

        paths = list()

        def _recurse(x, y, path_formed, visited, obs):
            #print x,y, path_formed, visited
            # return if invalid
            if x<0 or y<0 or x>m-1 or y>n-1:
                return

            # return if visited
            if visited[x][y]:
                return

            # return if obstacle
            if obs <= 0:
                return

            if grid[x][y] == 1:
                obs -= 1
            #print obs

            visited_local = copy.deepcopy(visited)
            path_formed_local = copy.deepcopy(path_formed)

            path_formed_local.append((x,y))
            visited_local[x][y] = True
            if x==m-1 and y==n-1:
                print 'FOUND={}'.format(path_formed_local)
                paths.append(path_formed_local)
            else:
                _recurse(x-1, y, path_formed_local, visited_local, obs)
                _recurse(x, y-1, path_formed_local, visited_local, obs)
                _recurse(x-1, y-1, path_formed_local, visited_local, obs)
                _recurse(x+1, y, path_formed_local, visited_local, obs)
                _recurse(x, y+1, path_formed_local, visited_local, obs)
                _recurse(x+1, y+1, path_formed_local, visited_local, obs)

        visited = [ [None for _ in range(n)] for _ in range(m) ]
        #print visited
        #print visited[2][3]
        _recurse(0, 0, list(), visited, k)

        min_length = None
        for path in paths:
            l = len(path)
            if min_length:
                if l < min_length:
                    min_length = l
            else:
                min_length = l

        if min_length:
            return min_length
        else:
            return -1


"""
https://leetcode.com/contest/weekly-contest-167/problems/sequential-digits/
"""

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        sl = str(low)
        sh = str(high)

        nl = len(sl)
        nh = len(sh)

        l_first = int(sl[0])
        h_first = int(sh[0])

        output = list()

        for total_digits in range(nl, nh+1):
            #print 'td={}, lf={}, hf={}'.format(total_digits, l_first, h_first)
            # start with l_first as first digit
            for first_digit in range(l_first, 9-l_first):
                #print 'fd={}'.format(first_digit)
                num_list = list()
                # create number with total count as total_digits
                current_digit = first_digit
                for _ in range(total_digits):
                    num_list.append(current_digit)
                    current_digit += 1

                #print num_list
                new_num = int(''.join([str(n) for n in num_list]))
                #print new_num

                if low <= new_num <= high:
                    output.append(new_num)

        return output



"""
https://leetcode.com/contest/weekly-contest-167/problems/convert-binary-number-in-a-linked-list-to-integer/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        curr = head
        self.result = 0
        i = 0

        def _recurse(node, m2):
            if node:
                m2_recv = _recurse(node.next, m2)
                if not m2_recv:
                    m2_recv = m2
                self.result += m2_recv*node.val
                #print 'res={}, m2={}, n={}'.format(self.result, m2_recv, node.val)
                m2_recv *= 2
                return m2_recv

        _recurse(head, 1)
        #print self.result
        return self.result
"""
"""