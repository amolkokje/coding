
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
        #visited = [False for _ in range(arrLen)]
        self.count = 0

        def _recurse(step_count, place, start):
            if step_count > steps:
                return

            if place<0 or place>=arrLen:
                return

            #print 'place={}, step_count={}'.format(place, step_count)
            if step_count == steps:
                if place==start:
                    self.count += 1
                    #print 'found, count={}'.format(self.count)
                    return

            _recurse(step_count+1, place-1, start)
            _recurse(step_count+1, place+1, start)
            _recurse(step_count+1, place, start)

        _recurse(0, 0, 0)
        return self.count





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
                #print 'wl={}'.format(word_local)
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
                    #print '--> word={}'.format(prefix + post_formed)
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

        #trie.print_all()
        #return

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
        n = len(grid[0]) # cols

        #print 'm={}, n={}'.format(m,n)

        #row_servers = [ 0 for _ in range(m) ]
        #col_servers = [ 0 for _ in range(n) ]

        #for i in range(m):
        #    row_servers[i] = len( filter(lambda x:x==1, grid[i]) )

        #for i in range(n):
        #    col_servers[i] = len( filter(lambda x:x==1, [ grid[k][i] for k in range(m) ]) )

        comm_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    print '---> ({},{})'.format(i,j)

                    """
                    r_before = grid[i][:j]
                    #print 'r_before={}'.format(r_before)
                    if 1 in r_before:
                        comm_count += 1
                    """

                    r_after = grid[i][j+1:]
                    #print 'r_after={}'.format(r_after)
                    if 1 in r_after:
                        comm_count += 1

                    """
                    col_before = [ grid[k][j] for k in range(i) ] ###
                    #print 'col_before={}'.format(col_before)
                    if 1 in col_before:
                        comm_count += 1
                    """

                    col_after = [ grid[k][j] for k in range(i+1,m) ]
                    #print 'col_after={}'.format(col_after)  ## ??
                    if 1 in col_after:
                        comm_count += 1

                print 'i={},j={}, count={}'.format(i,j,comm_count)
        return comm_count



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
        #visited = [ False for _ in range(n) ]

        current = points[0]
        steps = 0
        for point in points[1:]:
            #print 'trynig to reach {}'.format(point)

            while True:
                #print 'current: {}'.format(current)

                if current == point:
                    #steps += 1
                    #print '--> reached: {}'.format(current)
                    break

                if current[0] < point[0]:
                    next_x = current[0]+1
                elif current[0] > point[0]:
                    next_x = current[0]-1
                else:
                    next_x = current[0]

                if current[1] < point[1]:
                    next_y = current[1]+1
                elif current[1] > point[1]:
                    next_y = current[1]-1
                else:
                    next_y = current[1]

                current = [next_x, next_y]
                steps += 1

        return steps




