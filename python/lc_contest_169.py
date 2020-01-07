"""
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_bst_list(self, root):
        output = list()
        curr = root

        def _recurse(node):
            if node:
                _recurse(node.left)
                output.append(node.val)
                _recurse(node.right)

        _recurse(root)
        return output

    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """

        bl1 = self.get_bst_list(root1)
        bl2 = self.get_bst_list(root2)

        n1 = len(bl1)
        n2 = len(bl2)

        i1 = 0
        i2 = 0
        output = list()
        while i1 < n1 and i2 < n2:
            if bl1[i1] <= bl2[i2]:
                output.append(bl1[i1])
                i1 += 1
            else:
                output.append(bl2[i2])
                i2 += 1

        while i1 < n1:
            output.append(bl1[i1])
            i1 += 1
        while i2 < n2:
            output.append(bl2[i2])
            i2 += 1

        return output


"""
https://leetcode.com/contest/weekly-contest-169/problems/jump-game-iii/
"""


class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        max_tries = n = len(arr)

        def _recurse(i, tries):
            if tries > max_tries:
                return False

            index_left = i - arr[i]
            if index_left < 0:
                index_left = 0

            index_right = i + arr[i]
            if index_right >= n:
                index_right = n - 1

            if arr[index_left] == 0 or arr[index_right] == 0:
                return True

            return _recurse(index_left, tries + 1) or _recurse(index_right, tries + 1)

        return _recurse(start, 0)


"""
https://leetcode.com/contest/weekly-contest-169/problems/find-n-unique-integers-sum-up-to-zero/
"""

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = list()

        if n % 2 != 0:
            arr.append(0)

        c = (n / 2) + 1
        print c
        for i in range(1, c):
            arr.append(-i)
            arr.append(i)

        return sorted(arr)
