"""
Examples:
    # Duplicate Keys returns a list of values
    # Values are sorted
    In: {"a": "1", "b": "2", "c": "2"}
    Out: {"1": "a", "2": ["b", "c"]}

    # No Duplicates, so values are strings
    In: {"a": "1", "b": "2", "c": "3"}
    Out: {"1": "a", "2": "b", "3": "c"}

"""

# Read input from STDIN. Print output to STDOUT
# Valid input is a JSON string
# Method should load JSON string into Python dict
# Method should invert Python dict
# When duplicate keys exist, value should be a list of all values
# When value is a list, the list should be sorted
# Method should return a *sorted* JSON string
import json

def invert_dict(json_string):
    #print 'ip={}, type={}'.format(json_string, type(json_string))
    json_input = json.loads(json_string)

    json_output = dict()
    for k, v in json_input.iteritems():
        key = str(k)
        val = str(v)

        exists_val = json_output.get(val)
        if exists_val:
            if isinstance(exists_val, str):
                json_output[val] = [exists_val]
            json_output[val].append(key)
        else:
            json_output[val] = key


    # Invert dict
    return str(json_output) # JSON String

input_data = raw_input()  # Get data from stdin

# Print results to stdout
print(invert_dict(input_data))






Username: ubuntu

Server: 3.80.249.51

Password: 5awihr

Command: ssh ubuntu@3.80.249.51


{"1": "a", "3": "c", "2": "b"}

json_string
esdfsdfs

#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        is_multiple_3 = False
        is_multiple_5 = False
        output = ''

        if i<3:
            output = i
        elif 3<=i<5:
            if i%3==0:
                is_multiple_3=True
                output = 'Fizz'
            else:
                output = i
        else:
            is_multiple_3 = (i%3==0)
            is_multiple_5 = (i%5==0)
            if is_multiple_3 and is_multiple_5:
                output = 'FizzBuzz'
            else:
                if is_multiple_3:
                    output = 'Fizz'
                elif is_multiple_5:
                    output = 'Buzz'
                else:
                    output = i
        print output

if __name__ == '__main__':
    n = int(raw_input().strip())

    fizzBuzz(n)

