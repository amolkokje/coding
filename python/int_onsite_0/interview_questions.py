import sys, os

"""
Master Mind Game:
Hits - 1 Black Peg
Pseudo Hits - 1 White Peg

Code:  [0, 1, 2, 3]
Guess: [1, 2, 1, 4]
Output: 2W


Code:  [0, 1, 2, 3]
Guess: [0, 2, 3, 1]
Output: 1B3W

Code:  'RGBY'
Guess: 'GGRR'
Output: 1B1W

Code:  'RGGY'
Guess: 'GGRR'
Output: 1B2W
"""

"""
Q: Approach on how will you optimize and drop guesses that cannot be code, based on the history of guesses
Say that for a guess 1100 I have 0B0W. 0B along with OW implies that none of the digits in the Guess exist in the Code.
Hence for all the Guess that contain 0 and 1 only, can be responded by 0B0W. Only the ones that do not contain any 0 or
1 can be run through the mastermind() method

PSEUDO CODE:
class Mastermind(object):
    def __init__(self):
        self.bad_guess_list = list()
        
    def _execute(self, code, guess):
        # mastermind algo
        
    def check(self, code, guess):
        # check for bad guess
        for bad_guess in self.bad_guess_list():
            for g in range(guess):
                if g in bad_guess:
                    return '0B0W'
        
        # if not a bad guess, run the mastermind algo
        result = self._execute(code, guess)
        if result == '0B0W':
            self.bad_guess_list.append(guess)
        return result
"""

def mastermind(code, guess):

    # store hits and psuedo-hits in dict, with { Index-of-Code: Value-of-Code }
    hits_dict = dict()
    phits_dict = dict()

    n = len(code)  # len code==guess, and is always 4 so interviewer was not bothered about scalability of N/n

    # hits
    for i in range(n):
        if guess[i] == code[i]:
            hits_dict[i] = code[i]

    # psuedo-hits
    for i in range(n):
        # Conditions to check:
        # 1. Its not already a hit
        # 2. Its not already considered a psuedo-hit

        # check if the value exists in code
        if guess[i] in code:

            # check in code to find the index
            for j in range(n):  # iterate over the code
                # check-1: not a hit
                # check-2: not already considered a phit
                # check-3: not already considered a hit
                if j!=i and (code[j]==guess[i]) and (j not in phits_dict.keys()) and (j not in hits_dict.keys()):
                    phits_dict[j] = code[j]
                    break

    print 'HITS={}, P-HITS={}'.format(hits_dict, phits_dict)

    # convert to score and return
    return '{}B{}W'.format(len(hits_dict.keys()), len(phits_dict.keys()))

"""
Q: Word Suggestions from a dictionary: Implement methods for add_word(), get_suggestions(), remove_word()
"""

sys.path.append('../')
from trie_problems import Trie

class WordDictionary(object):

    def __init__(self):
        self.trie = Trie()

    def add_word(self, word):
        self.trie.insert(word)

    def get_suggestions(self, prefix):
        return self.trie.search_prefix(prefix)

    def remove_word(self, word):
        self.trie.remove(word)

    def print_all(self):
        return self.trie.show()

"""
Q: Given an array with odd and even numbers. Write code to update it such that the even elements on right and odd are 
on left. Temp var is fine, but not more. 
- Need to shift in place. Order of odd or even numbers after shift does not matter in the array.
- e.g. arr = [1,3,4,2,5] output = [1,3,5,4,2]
- e.g. arr = [1,3,4,2,6] output = [1,3,4,2,6]
"""

# pythonic
def update_arr(arr):
    n = len(arr)-1  # get index of last element
    i = 0

    def _is_even(n):
        return True if n%2==0 else False

    while i<n:
        if _is_even(arr[i]):
            # if the last element is even, cannot replace with it
            if _is_even(arr[n]):
                k = n-1
                # find the closest non-even
                while k>i:
                    if not _is_even(arr[k]):
                        break
                    k -= 1
                # if unable to find non-even on the right, return
                if k == i:
                    return
                else:
                    n = k

            arr[i], arr[n] = arr[n], arr[i]
        i += 1





if __name__ == '__main__':

    for arr in [ [1,3,4,2,5], [1,3,4,2,6] ]:
        print 'Arr={}'.format(arr)
        update_arr(arr)
        print 'After Update: Arr={}'.format(arr)

    print '##################################################################'

    words = ['amol', 'amolkokje', 'kokje', 'akokje', 'kokjeak']
    word_dictionary = WordDictionary()
    for word in words:
        word_dictionary.add_word(word)

    print 'WORDS IN DICTIONARY = {}'.format(word_dictionary.print_all())
    print 'SUGGESTIONS FOR PREFIX {} = {}'.format('kokj', word_dictionary.get_suggestions('kokj'))

    for word in ['kokjeak', 'amol', 'amolkokje']:
        word_dictionary.remove_word(word)
        print 'AFTER REMOVING {}: WORDS IN DICTIONARY = {}'.format(word, word_dictionary.print_all())

    print '##################################################################'

    iplist = [ # (Code, Guess)
        ([0, 1, 2, 3], [1, 2, 1, 4]),
        ([0, 1, 2, 3], [0, 2, 3, 1]),
        ('RGBY', 'GGRR'),
        ('RGGY', 'GGRR')
    ]

    for ip in iplist:
        print "\n"
        print 'CODE={}, GUESS={}, OUTPUT={}'.format(ip[0], ip[1], mastermind(ip[0], ip[1]))








"""
Interviewer - 1 (JJ) - Leadership
Q: Time when you were not able to get an agreement to move forward with a design or process? What did you do?
- AWS Elasticsearch: index directly, no S3. 
- Gave interim solution

Q: Say you have to work on a project across team, and there are disagreements. If you were a manager on one of the teams what would you do?
Q: Same as before: If you were a common manager to both, how would you handle it?

Interviewer -2:
Q: Master Mind Game
Q: Approach on how will you optimize and drop guesses that cannot be code, based on the history of guesses

Interviewer-3:
Q: Word Suggestions from a dictionary: Implement methods for add_word(), get_suggestions(), remove_word()

Interviewer-4 (Davit):
Q: Given a list of nodes. Write code to find out number of reciprocating edges. A reciprocating edge is an edge where there are connections existing from a node to other in either direction. 

Q: Write test cases for the function. 

Interviewer-5:
Q: One more?

Q: Given an array with odd and even numbers. Write code to update it such that the even elements on right and odd are on left. Temp var is fine, but not more. 
- Need to shift in place. Order of odd or even numbers after shift does not matter in the array.
- e.g. arr = [1,3,4,2,5] output = [1,3,5,4,2]
- e.g. arr = [1,3,4,2,6] output = [1,3,4,2,6]


Q: Given a document with several lines, and a file containing words on each line. Write code to write another file 
wherein the words listed in the input file are replaced by *.
- The input file can be very big so loading it in memory is not allowed. Its possible that there can be many big 
lines where each line is also too big to load in memory.
- The input file containing words cannot be too big.
"""



