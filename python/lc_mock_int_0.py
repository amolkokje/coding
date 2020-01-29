import sys

"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you
take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first
turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can
win the game given the number of stones in the heap.

Example:

Input: 4
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be
             removed by your friend.
"""


class Solution(object):
    @staticmethod
    def canWinNim(n):
        """
        :type n: int
        :rtype: bool
        """
        poss = [1, 2, 3]

        def _recurse(stones, taken):

            for take in poss:
                if stones-take == 0:
                    if taken:
                        return False
                    else:
                        return True

            taken = not taken

            return _recurse(stones-1, taken) or _recurse(stones-2, taken) or _recurse(stones-3, taken)

        return _recurse(n-1, True) or _recurse(n-2, True) or _recurse(n-3, True)
    

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

EXAMPLE:
INPUT: x = 1, y = 4
OUTPUT: 2
0 <= x < 2^31
EXPLANATION:
1   (0 0 0 1)
4   (0 1 0 0)
       *   *   --> distance=2
The above stars point to positions where the corresponding bits are different.
"""


class Solution2(object):
    def _convert_int_to_bin(self, x):
        bin_str = bin(x).split('b')[1]
        n = len(bin_str)
        diff = 32 - n
        if diff > 0:
            bin_str = ''.join(['0' for _ in range(diff)]) + bin_str
        return bin_str

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = self._convert_int_to_bin(x)
        y = self._convert_int_to_bin(y)

        tstart = None
        min_diff = 33
        for i in range(32):
            if x[i] != y[i]:
                if not tstart:
                    tstart = i
                else:
                    diff = i - tstart
                    if diff < min_diff:
                        min_diff = diff
                        tstart = i
                        # print tstart
        if min_diff == 33:
            return None
        return min_diff


"""
Int-1: 
"""
"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should 
be set to NULL.

Initially, all next pointers are set to NULL.

** Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 
Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to 
point to its next right node, just like in Figure B. The serialized output is in level order as connected by the 
next pointers, with '#' signifying the end of each level.
 
Constraints:
The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution3(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # print root

        # list containing node list at each level
        node_level_list = list()

        # recurse through left first and then to right, so left nodes go in the
        # list before the right ones
        def _recurse(node, level):
            if node:
                if level >= len(node_level_list):
                    node_level_list.append(list())

                # print len(node_level_list), node_level_list
                node_level_list[level].append(node)

                _recurse(node.left, level + 1)
                _recurse(node.right, level + 1)

        _recurse(root, 0)

        output = list()
        # update node right vals
        for node_list in node_level_list:
            n = len(node_list)
            for i in range(n - 1):
                node_list[i].right = node_list[i + 1]
            new_node = Node(val='#')
            node_list[-1].right = new_node
            node_list.append(new_node)
            output.extend(node_list)

        return output


if __name__ == '__main__':
    sol = Solution()
    for ip in [4, 8]:
        print 'ip={}, out={}'.format(ip, sol.canWinNim(ip))
    sys.exit()

    sol2 = Solution2()
    for ip in [[1, 4], [3, 1], [4, 2]]:
        print 'ip={}, hamming distance={}'.format(ip, sol2.hammingDistance(ip[0], ip[1]))
