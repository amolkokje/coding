"""
https://www.geeksforgeeks.org/decode-string-recursively-encoded-count-followed-substring/
CHALLENGE: In this exercise, you're going to decompress a compressed string.

Your input is a compressed string of the format number[string] and the decompressed output form should be the
string written number times. For example:

INPUT: 3[abc]4[ab]c
OUTPUT: abcabcabcababababc

OTHER RULES:
- Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa
- One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab
- Characters allowed as input include digits, small English letters and brackets [ ].
- Digits are only to represent amount of repetitions.
- Letters are just letters.
- Brackets are only part of syntax of writing repeated substring.
- Input is always valid, so no need to check its validity.
"""

import re, sys, os


def decode(Str):
    integerstack = []
    stringstack = []

    # Traversing the string
    for i in range(len(Str)):

        # If number, convert it into number and push it into integerstack.
        if Str[i].isdigit():
            nums = list()
            while Str[i].isdigit():
                nums.append(Str[i])
                i += 1

            i -= 1
            count = int(''.join(nums))
            if count:
                integerstack.append(count)
            #print 'integer stack = [{}]'.format(integerstack)

        # If closing bracket ']', pop element until '[' opening bracket is not found in the character stack.
        elif Str[i] == ']':
            temp = ""

            # get the last number from integer stack
            if len(integerstack) > 0:
                count = integerstack.pop(-1)

            # go from '[' to ']' and store the string in a temp var in reverse order
            while len(stringstack)>0 and stringstack[-1]!='[':
                temp = stringstack.pop(-1) + temp

            # get rid of the opening bracket
            if len(stringstack)>0 and stringstack[-1]=='[':
                stringstack.pop(-1)

            # Decode the string i.e. multiply the multiplier count(repeats) with the string
            # Push it to the stringstack, so it can be decompressed further if there are brackets outside
            if count:
                stringstack += [count*temp]

        else:
            stringstack.append(Str[i])

    # Join all to make single string, and return
    return ''.join(stringstack)


if __name__ =='__main__':
    inputs = [
        '3[abc]4[ab]c',
        '3[a]b',
        '2[3[a]b]',
        '10[a]'
    ]
    for input in inputs:
        print 'Compressed Input=[{}], Decompressed Output=[{}]'.format(input, decode(input))

