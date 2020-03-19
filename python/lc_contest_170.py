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
        n = len(watchedVideos)
        videos = set()
        visited = [ False for _ in range(n) ]

        def _recurse(fid, rlevel):
            if visited[fid]:
                return

            #print 'fid={}, rlevel={}, friends={}'.format(fid, rlevel, friends[fid])
            if rlevel == level:
                for v in watchedVideos[fid]:
                    videos.add(v)
                return

            visited[fid] = True
            for nfid in friends[fid]:
                _recurse(nfid, rlevel+1)
            visited[fid] = False

        _recurse(id, 0)
        return list(videos)


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
