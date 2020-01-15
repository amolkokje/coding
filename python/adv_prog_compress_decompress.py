"""
https://techdevguide.withgoogle.com/paths/advanced/compress-decompression#!
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


def find_all_decompress_candidates(input):
    #return re.findall(r'\d+\D+]', input)

    # find out if need to decompress
    opening = len(filter(lambda x: x=='[', input))
    closing = len(filter(lambda x: x==']', input))
    print 'opening={}, closing={}'.format(opening, closing)
    if not(opening>0 and closing>0 and opening==closing):
        return [(False, 0, input)]

    # split string
    candidates = list()  # tuples: (needs, str)
    i = 0

    start = None
    buffer = ''
    nums = ''
    ob = 0
    cb = 0
    while i<len(input):
        if not start:
            if input[i]=='[':
                ob += 1
                start = i
                if len(buffer)>2:
                    print 'buffer={}'.format(buffer)
                    candidates.append(False, 0, buffer[-2])
                    buffer = ''
            else:
                buffer += input[i]
                if input[i].isdigit():
                    nums+=input[i]

        elif start:
            if ob!=cb:
                if input[i]=='[':
                    ob+=1
                    if ob==1:
                        start=i
                elif input[i]==']':
                    cb+=1
                    if ob==cb:
                        candidates.append((True, int(''.join(nums)), input[start+1:i]))
                        nums=''
                        start = None
                        ob=0
                        cb=0
        print start, buffer
        i+=1

    if len(buffer)>1:
        print buffer
        candidates.append((False, 0, buffer[1:]))
    print 'input={}, candidates={}'.format(input, candidates)
    return candidates


def decompress(input):
    output = ''
    n = len(input)

    candidates = find_all_decompress_candidates(input)
    for candidate in candidates:
        raw_input('Candidate={}'.format(candidate))
        needs, count, string = candidate

        if '[' in string and ']' in string:
            string = decompress(string)

        if needs:
            output += ''.join([ string for _ in range(count) ])
        else:
            output += string
    print 'output={}'.format(output)
    return output



if __name__ =='__main__':
    inputs = [
        #'3[abc]4[ab]c',
        '3[a]b',
        '2[3[a]b]',
        '10[a]'
    ]
    for input in inputs:
        print '*******'
        print '---> IN:{}'.format(input)
        print 'OUT:{}'.format(decompress(input))
        raw_input('***')
