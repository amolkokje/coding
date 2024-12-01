"""
Interviewer - 1 (JJ) - Leadership
Q: Time when you were not able to get an agreement to move forward with a design or process? What did you do?
- AWS Elasticsearch: index directly, no S3. 
- Gave interim solution

Q: Say you have to work on a project across team, and there are disagreements. If you were a manager on one of the teams what would you do?
Q: Same as before: If you were a common manager to both, how would you handle it?


Interviewer-3:
Q: Word Suggestions from a dictionary: Implement methods for add_word(), get_suggestions(), remove_word()
---> TRIE
"""

"""
Interviewer-4 (Davit):
Q: Given a list of nodes. Write code to find out number of reciprocating edges. 
A reciprocating edge is an edge where there are connections existing from a node to other in either direction. 
"""
# TODO: need the whole problem


"""
Q: Given an array with odd and even numbers. Write code to update it such that the even elements on right and odd are on left. Temp var is fine, but not more. 
- Need to shift in place. Order of odd or even numbers after shift does not matter in the array.
- e.g. arr = [1,3,4,2,5] output = [1,3,5,4,2]
- e.g. arr = [1,3,4,2,6] output = [1,3,4,2,6]
"""


def rearrange(arr):
    print(f"rearrange: input={arr}")
    n = len(arr)
    l, r = 0, n - 1
    i = 0

    while i < n and i < r:
        if arr[i] % 2 == 0:
            arr[i], arr[r] = arr[r], arr[i]
            i += 1
            r -= 1
        else:
            arr[i], arr[l] = arr[l], arr[i]
            i += 1
            l += 1
    print(f"rearrange: output={arr}")


"""
Q: Given a document with several lines, and a file containing words on each line. Write code to write another file 
wherein the words listed in the input file are replaced by *.
- The input file can be very big so loading it in memory is not allowed. Its possible that there can be many big 
lines where each line is also too big to load in memory.
- The input file containing words cannot be too big.
"""


# to read a file in chunks, use fh.read(chunksize=X) or fh.readlines(lines=X) to void reading whole file contents in memory and causing the program to fail
def parse_large_file(inputfile, wordsfile, outputfile):
    wordset = set()
    with open(wordsfile, "r") as fh:
        for w in fh.readlines():  # words file is not to big
            wordset.add(w)

    with open(outputfile, "w") as foutput:
        with open(inputfile, "r") as finput:
            while True:
                inputchunk = finput.readlines(1000)  # read 1000 lines at a time
                if inputchunk is None:
                    break

                for line in inputchunk:
                    foundword = False
                    words = line.split()
                    for word in words:
                        if word in wordset:
                            foundword = True
                            break
                    if foundword is True:
                        outputline = line
                        for word in wordset:
                            outputline = outputline.replace(word, "*")
                        foutput.write(outputline)


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

Interviewer -2:
Q: Master Mind Game
Q: Approach on how will you optimize and drop guesses that cannot be code, based on the history of guesses
"""


def mastermind(code, guess):
    n = len(code)
    black = 0  # hits
    white = 0  # pseudo-hits

    # count total in the code
    cdict = {}
    for c in code:
        cdict[c] = cdict.get(c, 0) + 1
    print(f"mastermind: code={code}, cdict={cdict}")

    # check if guess is in the code
    # check hits
    for i in range(n):
        if guess[i] == code[i]:
            black += 1
            cdict[guess[i]] -= 1
            if cdict[guess[i]] == 0:
                del cdict[guess[i]]
    print(f"mastermind: code={code}, after hits: cdict={cdict}")

    # check pseudo-hits
    for i in range(n):
        # skip the hits
        if guess[i] == code[i]:
            continue
        # check if its a pseudo-hit
        if guess[i] in cdict:
            white += 1
            cdict[guess[i]] -= 1
            if cdict[guess[i]] == 0:
                del cdict[guess[i]]
    print(f"mastermind: code={code}, after psuedo-hits: cdict={cdict}")

    result = ""
    if black > 0:
        result += f"{black}B"
    if white > 0:
        result += f"{white}W"
    print(f"mastermind: code={code}, guess={guess}, result={result}")
    return result


if __name__ == "__main__":
    print("---------------------------------")
    for arr in [[1, 3, 4, 2, 5], [1, 3, 4, 2, 6]]:
        rearrange(arr)

    for code, guess, result in [  # (Code, Guess)
        ([0, 1, 2, 3], [1, 2, 1, 4], "2W"),
        ([0, 1, 2, 3], [0, 2, 3, 1], "1B3W"),
    ]:
        assert result == mastermind(code, guess)
