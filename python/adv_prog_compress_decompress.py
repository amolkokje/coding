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


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def find_all_decompress_candidates(input):
    return re.findall(r'\d+\D+]', input)

def needs_more_decompress(input):
    # if there is a number in the string
    needs = False
    for i in input:
        if is_number(i):
            needs = True
    print 'STR={}, NEEDS={}'.format(input, needs)
    return False

def multiply_by_count(input):
    match_result = re.match(r'(\d+)(.*)', input)
    count, multiply_str = match_result.groups()
    multiply_str = multiply_str[1:-1]   # remove starting [ and ending ]
    #print count, multiply_str
    output = int(count)*multiply_str
    print 'IN={}, OUT={}'.format(input, output)
    return output

def decompress(input):
    output = ''
    n = len(input)

    decompress_candidates = find_all_decompress_candidates(input)
    # if sum of all lengths is the equal to total length, then all need to be decompressed.
    # if not the same, then there are some in the beginning/end that dont need to decompressed
    print decompress_candidates

    for candidate in decompress_candidates:
        if needs_more_decompress(candidate):
            output += decompress(candidate)
        else:
            output += multiply_by_count(candidate)
    return output



if __name__ =='__main__':
    inputs = [
        #'3[abc]4[ab]c',
        '2[3[a]b]',
        '10[a]'
    ]
    for input in inputs:
        print '*******'
        print '---> IN:{}, OUT:{}'.format(input, decompress(input))
