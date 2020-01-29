"""
https://leetcode.com/contest/weekly-contest-171/problems/minimum-distance-to-type-a-word-using-two-fingers/
"""
# FAILS FOR: "JDX"

from string import ascii_uppercase


class Solution(object):
    def get_cd(self, c, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == c:
                    return (i, j)

    def get_distance(self, p0, p1):
        return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])

    def get_letter_matrix(self):
        mat = list()
        m = 6  # rows
        k = 0
        row = None
        for a in ascii_uppercase:
            if k % 6 == 0:
                if row:
                    mat.append(row)
                row = list()

            row.append(a)
            k += 1
        row += ['' for _ in range(4)]
        mat.append(row)
        return mat

    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """

        # get all the letters from A to Z in a matrix
        mat = self.get_letter_matrix()
        m = len(mat)  # rows
        n = len(mat[0])  # cols
        print m, n

        # distance counters for left and right fingers
        left_hand_pts = list()
        right_hand_pts = list()

        # get movement of left and right hands
        for w in word:
            x, y = self.get_cd(w, mat)
            # print '({},{}), n/2={}'.format(x, y, n/2)
            if y < n / 2:  # point is on left side
                left_hand_pts.append((x, y))
            else:
                right_hand_pts.append((x, y))

        # NOTE: optimize this for min distance, but this is not needed for normal keyboard type operation
        # where the left hand remains on the left, and right hand remains on the right side.
        # Hence. Answer incorrect for: "PRDL", "JDX", etc
        if not left_hand_pts and right_hand_pts:
            left_hand_pts.append(right_hand_pts.pop(-1))
        elif not right_hand_pts and left_hand_pts:
            right_hand_pts.append(left_hand_pts.pop(-1))

        # print 'left={}, right={}'.format(left_hand_pts, right_hand_pts)

        # get distance traversed by each hand
        def _get_distance(pts):
            k = len(pts)
            i = 1
            dist = 0
            while i < k:
                dist += self.get_distance(pts[i - 1], pts[i])
                i += 1
            return dist

        return _get_distance(left_hand_pts) + _get_distance(right_hand_pts)


"""
https://leetcode.com/contest/weekly-contest-171/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
"""


class Solution(object):
    def is_no_zero(self, x):
        arr_x = [int(s) for s in str(x)]
        temp = filter(lambda x: x != 0, arr_x)
        return len(arr_x) == len(temp)

    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1, n):
            if self.is_no_zero(i) and self.is_no_zero(n - i):
                return [i, n - i]


"""
https://leetcode.com/contest/weekly-contest-171/problems/number-of-operations-to-make-network-connected/
"""


# AMOL - GOOD ONE

class Solution(object):
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1

        # create a list of nodes and its connections
        node_connections = [list() for _ in range(n)]
        for a, b in connections:
            node_connections[a].append(b)
            node_connections[b].append(a)

        # recurse through each node, and mark as visited if found a connection to
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for neighbor in node_connections[node]:
                dfs(neighbor)

        visited = [False for _ in range(n)]
        min_new_connections = 0
        for i in range(n):
            # if a node is not visited, then it points to broken connection
            if not visited[i]:
                dfs(i)
                min_new_connections += 1

        # -1 to compensate for the first iteration
        return min_new_connections - 1


"""
https://leetcode.com/contest/weekly-contest-171/problems/minimum-flips-to-make-a-or-b-equal-to-c/
"""


class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        astr = '{:032b}'.format(a)
        bstr = '{:032b}'.format(b)
        cstr = '{:032b}'.format(c)

        min_flips = 0
        for i in range(len(cstr)):
            if cstr[i] == '0':
                if astr[i] != bstr[i]:
                    min_flips += 1
                elif astr[i] == bstr[i] == '1':
                    min_flips += 2


            elif cstr[i] == '1':
                if astr[i] == bstr[i]:
                    if astr[i] != '1':
                        min_flips += 1

                        # print 'c={}, a={}, b={} --> mf={}'.format(cstr[i], astr[i], bstr[i], min_flips)
        return min_flips
