"""
https://leetcode.com/contest/weekly-contest-170/problems/get-watched-videos-by-your-friends/
"""


class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        n = len(friends)

        fof = set()
        queue = [[id]]
        for l in range(level):
            friends_id = queue.pop(0)
            # print 'level={}, friends={}'.format(l, friends_id)
            friends_next_level_id = list()
            for fid in friends_id:
                friends_next_level_id += friends[fid]
            print friends_next_level_id
            queue.append(list(set(friends_next_level_id)))

        # now queue[0] has the friends at the intended level

        # if cyclic and return back to the same point, delete the starting point
        target_friends = queue[0]
        for i in range(len(target_friends)):
            if target_friends[i] == id:
                target_friends.pop(i)
                break

        # get all movies of friends at that level
        videod = dict()
        for fid in target_friends:
            print 'fid={}'.format(fid)
            for video in watchedVideos[fid]:
                if not videod.get(video):
                    videod[video] = 1
                else:
                    videod[video] += 1

        return sorted(videod, key=videod.__getitem__)


"""
https://leetcode.com/contest/weekly-contest-170/problems/minimum-insertion-steps-to-make-a-string-palindrome/
"""

"""
https://leetcode.com/contest/weekly-contest-170/problems/xor-queries-of-a-subarray/
"""


class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        return [reduce(lambda x, y: x ^ y, arr[query[0]: query[1] + 1]) for query in queries]


"""
https://leetcode.com/contest/weekly-contest-170/problems/decrypt-string-from-alphabet-to-integer-mapping/
"""

# 'c' -> ord('c')-96
from string import ascii_lowercase

dg_dict = None


class Solution(object):
    def get_digit_str_map(self):
        dg_dict = dict()
        for s in ascii_lowercase:
            val = ord(s) - 96
            if val >= 10:
                dg_dict[str(val) + '#'] = s
            else:
                dg_dict[str(val)] = s
        # print dg_dict
        return dg_dict

    def convert_digit_to_str(self, d):
        global dg_dict
        if not dg_dict:
            dg_dict = self.get_digit_str_map()

        # print 'in={}, out={}'.format(d, dg_dict[d])
        return dg_dict[d]

    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        output = ''
        window = 3
        i = 0
        while i < n:
            # print i
            current = s[i:i + window]
            if current[-1] == '#':
                output += self.convert_digit_to_str(current)
                i += window
            else:
                output += self.convert_digit_to_str(s[i])
                i += 1
        # print output
        return output
