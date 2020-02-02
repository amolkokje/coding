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


if __name__ == '__main__':

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


Q: Given a document with several lines, and a file containing words on each line. Write code to write another file wherein the words listed in the input file are replaced by ‘*’.
- The input file can be very big, so loading it in memory is not allowed. Its possible that there can be many big lines where each line is also too big to load in memory.
- The input file containing words cannot be too big.


"""



