
"""
https://leetcode.com/contest/weekly-contest-170/problems/get-watched-videos-by-your-friends/
"""

class Solution(object):

    def get_friends_of_friends(self, id, friends):
        my_friends = friends[id]
        my_ff = list()

        for fid in my_friends:
            my_ff.extend(friends[fid])
        return my_ff

    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        max_count = 0

        if level == 1:
            # get videos watched by friends
            wv_dict = dict()
            for fid in friends[id]:
                videos = watchedVideos[fid]
                for v in videos:
                    if wv_dict.get(v):
                        wv_dict[v] += 1
                    else:
                        wv_dict[v] = 1

        elif level==2:
            ff_list = list(set(self.get_friends_of_friends(id, friends)))
            n = len(ff_list)
            i= 0
            while i < n:
                if ff_list[i] == id:
                    n -= 1
                    ff_list.pop(i)
                i += 1
            #print ff_list

            wv_dict = dict()
            for fid in ff_list:
                videos = watchedVideos[fid]
                for v in videos:
                    if wv_dict.get(v):
                        wv_dict[v] += 1
                    else:
                        wv_dict[v] = 1

                        #return wv_dict.keys()
        #print wv_dict
        return sorted(wv_dict, key=wv_dict.__getitem__)



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
        output = list()
        for query in queries:
            #L = query[0]
            #R = query[1]+1
            #xor_out = reduce(lambda x,y:x^y, arr[L: R])
            #output.append(xor_out)
            output.append(reduce(lambda x,y:x^y, arr[query[0]: query[1]+1]))
            #print L, R, arr[L:R], xor_out

        return output

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
            val = ord(s)-96
            if val >= 10:
                dg_dict[str(val) + '#'] = s
            else:
                dg_dict[str(val)] = s
        #print dg_dict
        return dg_dict

    def convert_digit_to_str(self, d):
        global dg_dict
        if not dg_dict:
            dg_dict = self.get_digit_str_map()

        #print 'in={}, out={}'.format(d, dg_dict[d])
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
            #print i
            current = s[i:i+window]
            if current[-1] == '#':
                output += self.convert_digit_to_str(current)
                i += window
            else:
                output += self.convert_digit_to_str(s[i])
                i += 1
        #print output
        return output

