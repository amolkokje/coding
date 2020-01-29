
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
        m = len(grid)  #x -> rows
        n = len(grid[0])  #y -> cols
        visited = [ [False for _ in range(n)] for _ in range(m) ]

        paths = list()

        def _recurse(x, y, path_length, obs, path):

            # return if invalid
            if x<0 or y<0 or x>=m or y>=n:
                return

            # return if visited
            if visited[x][y]:
                return

            # return if max obstacle count is done
            if obs < 0:
                return

            # if obstacle, increment the obstacle count for tracking
            if grid[x][y] == 1:
                obs -= 1

            if x==m-1 and y==n-1:
                #print 'here: path={}'.format(path)
                paths.append(path + [(x,y)])

            else:
                next_points = [ (x-1,y), (x,y-1), (x+1,y), (x,y+1) ]
                for a,b in next_points:
                    visited[x][y] = True
                    path += [(x,y)]
                    _recurse(a, b, path_length+1, obs, path)
                    visited[x][y] = False
                    path.pop(-1)


        _recurse(0, 0, 0, k, list())
        #print 'paths={}'.format(paths)
        if paths:
            sorted_paths = sorted(paths, key=lambda x:len(x))
            return len(sorted_paths[0])-1
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


# if LL digits are in the reversed order
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """

        def _recurse(node, power, val):
            #print 'node={}, power={}, val={}'.format(node.val, power, val)
            if node:
                if node.val == 1:
                    power2 = 1
                    for p in range(power):
                        power2 *= 2
                    val += power2
                    return _recurse(node.next, power+1, val)
                else:
                    return _recurse(node.next, power+1, val)
            else:
                return val

        output = _recurse(head, 0, 0)
        #print 'out={}'.format(output)
        return output