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
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        poss = [1, 2, 3]

        def _recurse(num_left):
            print 'Me left = {}'.format(num_left)
            if num_left <= 0:
                return False

            # step-1: I remove
            if num_left in poss:
                return True

            # step-2: friend remove
            for me_remove_stone in poss:
                # num after I remove
                new_num_left = (num_left - me_remove_stone)

                # if num after friend removes is ==0 then not possible, >0 may be possible
                for friend_remove_stone in poss:
                    num_after_friend_remove_stone = new_num_left - friend_remove_stone
                    if num_after_friend_remove_stone > 0:
                        return _recurse(num_after_friend_remove_stone)

            return False

        return _recurse(n)


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


if __name__ == '__main__':
    sol = Solution()
    for ip in [4, 8]:
        print 'ip={}, out={}'.format(ip, sol.canWinNim(ip))

    sol2 = Solution2()
    for ip in [[1, 4], [3, 1], [4, 2]]:
        print 'ip={}, hamming distance={}'.format(ip, sol2.hammingDistance(ip[0], ip[1]))
