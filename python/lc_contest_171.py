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
        #print 'p0={}, p1={}'.format(p0, p1)
        return abs(p0[0]-p1[0]) + abs(p0[1]-p1[1])

    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """

        # get all the letters from A to Z in a matrix
        mat = list()
        m = 6 # rows
        k = 0
        row = None
        for a in ascii_uppercase:
            if k%6 == 0:
                if row:
                    mat.append(row)
                row = list()

            row.append(a)
            k += 1
        row += ['' for _ in range(4)]
        mat.append(row)
        print mat

        # distance counters for left and right fingers
        leftd = 0
        rightd = 0

        # first letter
        left = list()
        right = list()
        r, c = self.get_cd(word[0], mat)
        # If on left side of matrix, use the left finger
        if c < (m/2):
            left.append(word[0])
        else:
            right.append(word[0])

        # letters going forward
        dist = 0
        for w in word[1:]:
            pw = self.get_cd(w, mat)

            # if the next letter is closest to left finger, move using left finger, else right finger
            if left and right:
                ld = self.get_distance(pw, self.get_cd(left[-1], mat))
                rd = self.get_distance(pw, self.get_cd(right[-1], mat))
                if  ld <= rd:
                    left.append(w)
                    leftd += ld
                else:
                    right.append(w)
                    rightd += rd

            # if one of the finger is not used yet, then see which side the letter is and use that one
            elif left and not right:
                if pw[1] < m/2:
                    leftd += self.get_distance(pw, self.get_cd(left[-1], mat))
                    left.append(w)
                else:
                    right.append(w)

            elif right and not left:
                if pw[1] < m/2:
                    left.append(w)
                else:
                    rightd += self.get_distance(pw, self.get_cd(right[-1], mat))
                    right.append(w)


        return leftd+rightd

"""
https://leetcode.com/contest/weekly-contest-171/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
"""

class Solution(object):

    def is_no_zero(self, x):
        arr_x = [int(s) for s in str(x)]
        temp = filter(lambda x:x!=0, arr_x)
        return len(arr_x) == len(temp)

    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1, n):
            if self.is_no_zero(i) and self.is_no_zero(n-i):
                return [i, n-i]



"""
https://leetcode.com/contest/weekly-contest-171/problems/number-of-operations-to-make-network-connected/
"""
# UNDERSTAND WELL - SEE

class Solution(object):
    def makeConnected(self, n, connections):
        if len(connections) < n-1:
            return -1

        # create a list of nodes and its connections
        node_connections = [ list() for _ in range(n)]
        for a,b in connections:
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

                        #print 'c={}, a={}, b={} --> mf={}'.format(cstr[i], astr[i], bstr[i], min_flips)
        return min_flips





