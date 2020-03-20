# MOCK PASS: https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6NTExNzk3

"""
https://leetcode.com/contest/weekly-contest-164/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
"""

class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """

        ways = list()

        def _recurse(path):
            count_right = len(filter(lambda x:x=='R', path))
            count_left = len(filter(lambda x:x=='L', path))

            if len(path) == steps:
                if count_right == count_left:
                    ways.append(path)
                return

            # at start-point i.e. left, so cannot go more left
            if count_right == count_left:
                _recurse(path+['R'])

            # at right-most i.e. end of array, so cannot go more right
            elif count_right-count_left==arrLen:
                _recurse(path+['L'])

            # not at any corner, so can go in either direction
            else:
                _recurse(path+['R'])
                _recurse(path+['L'])

            # can always stay at the same location
            _recurse(path+['S'])

        # already at left-most side of array
        _recurse(['R'])
        _recurse(['S'])

        print 'Ways=[{}]'.format(ways)
        return len(ways)



"""
https://leetcode.com/contest/weekly-contest-164/problems/search-suggestions-system/
--> leetcode answer is wrong
"""
import copy


class TrieNode(object):
    def __init__(self, x):
        self.value = x
        self.child_nodes = list()
        self.is_word = False

    def __repr__(self):
        return '<TN: value={}, word={}>'.format(self.value, self.is_word)


class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        current = self.root
        for w in word:
            node_found = False
            for child in current.child_nodes:
                if child.value == w:
                    current = child
                    node_found = True
                    break
            if not node_found:
                new_child = TrieNode(w)
                current.child_nodes.append(new_child)
                current = new_child
        # at the last node
        current.is_word = True

    def print_all(self):
        current = self.root
        print 'current={}'.format(current.value)

        def _recurse(node, word):
            if node:
                word_local = copy.deepcopy(word)
                word_local += node.value
                # print 'wl={}'.format(word_local)
                if node.is_word:
                    print 'WORD={}'.format(word_local)

                if node.child_nodes:
                    for child in node.child_nodes:
                        _recurse(child, word_local)

        for child in current.child_nodes:
            _recurse(child, '')

    def search(self, prefix):
        current = self.root
        output = list()

        # go till the prefix last char node
        for p in prefix:
            node_found = False
            for child in current.child_nodes:
                if child.value == p:
                    current = child
                    node_found = True
                    break
            if not node_found:
                print 'Prefix {} not found!'.format(prefix)
                return

        # now current is at prefix last char
        # find all strings possible with this prefix

        def _recurse(post_formed, node):
            if node:
                post_formed += node.value
                if node.is_word:
                    # print '--> word={}'.format(prefix + post_formed)
                    output.append(prefix + post_formed)

                pf_local = copy.deepcopy(post_formed)
                for child in node.child_nodes:
                    _recurse(pf_local, child)

        for child in current.child_nodes:
            _recurse('', child)
        return output


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        trie = Trie()
        for p in products:
            print 'inserting {}'.format(p)
            trie.insert(p)

        # trie.print_all()
        # return

        output_list = list()
        word = ''
        for w in searchWord:
            word += w
            print 'word={}'.format(word)
            output = trie.search(word)
            print 'search output = {}'.format(output)
            output_list.append(output)
        return output_list


"""
https://leetcode.com/contest/weekly-contest-164/problems/count-servers-that-communicate/
"""


class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)  # rows
        n = len(grid[0])  # cols

        conn_count = 0

        for i in range(m):
            for j in range(n):

                # found a server
                if grid[i][j] == 1:

                    # check if it has at least 1 connection

                    # check if the row has a server
                    row_count = len(filter(lambda x: x == 1, grid[i]))
                    if row_count >= 2:
                        conn_count += 1
                    else:
                        # if row does not have any connections, check if col has any
                        col_count = len(filter(lambda x: x == 1, [grid[k][j] for k in range(m)]))
                        if col_count >= 2:
                            conn_count += 1

        return conn_count


"""
https://leetcode.com/contest/weekly-contest-164/problems/minimum-time-visiting-all-points/
"""


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        current = points[0]
        steps = 0
        for point in points[1:]:
            # print 'trying to reach {}'.format(point)

            while True:
                # print 'current: {}'.format(current)

                if current == point:
                    break

                if current[0] < point[0]:
                    next_x = current[0] + 1
                elif current[0] > point[0]:
                    next_x = current[0] - 1
                else:
                    next_x = current[0]

                if current[1] < point[1]:
                    next_y = current[1] + 1
                elif current[1] > point[1]:
                    next_y = current[1] - 1
                else:
                    next_y = current[1]

                current = [next_x, next_y]
                steps += 1

        return steps
