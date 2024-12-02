import sys, os, re, copy


"""
Write a function that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does 
not occur in A.
max N = 100000
Examples:
Given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [-1, -3], the function should return 1.
"""


def return_max_int(A):
    i = 1
    while i < 100000:
        if i not in A:
            return i
        i += 1
    return -1


"""
Given array of strings A, write function to calculate length of longest string S such that:
- S is concatenation of some strings of A
- every letter in S is different

Example 1:
A = [ 'co', 'dil', 'ity' ]
S could be 'codil', 'dilco', 'coity', 'ityco' --> 5

Example 2: 
A = [ abc, yyy, def, csv ]
S could be: abcdef, defabc, defcsv, csvdef  --> 6

Example 3:
A = [ potato, kayak, banana, racecar ]
S is: 0 (not possible)

Example 4: 
A = [ eva, jqw, tyn, jan ]
S is: evajqwtyn --> 9
"""


def all_letters_distinct(ip_str):
    # print (ip_str)
    return True if len(ip_str) == len(list(set(ip_str))) else False


def get_longest_concatenated_str_with_unique_letters(A):
    n = len(A)
    visited = [False for _ in range(n)]
    str_with_unique_letters = set()

    def _recurse(str_formed, i):
        if visited[i]:
            return

        if all_letters_distinct(str_formed + A[i]):
            str_with_unique_letters.add(str_formed + A[i])

            for j in range(i + 1, n):
                visited[i] = True
                _recurse(str_formed + A[i], j)
                visited[i] = False

    for i in range(n):
        _recurse("", i)

    # print str_with_unique_letters
    longest_len = 0
    for str_unique in str_with_unique_letters:
        l = len(str_unique)
        if l > longest_len:
            longest_len = l
    return longest_len


"""
Given arrays A and B of length N, find index K such that sum of A(0 to K-1) == sum A(K to N-1) == sum B(0 to K-1) == sum B(K to N-1)

Example 1: 
A=[4,-1,0,3], B=[-2,5,0,3]
K = 2

Example 2:
A=[2,-2,-3,3], B=[0,0,4,-4]
K = 2

Example 3:
A=[4,-1,-0,3], B=[-2,6,0,4]
K = 0 (not possible)

Example 4:
A=[1,4,2,-2,5], B=[7,-2,-2,2,5]
K = 2 
"""


def get_fair_index(A, B):
    n = len(A)

    # brute force - slow
    # for k in range(1,n-1):
    #     if sum(A[:k]) == sum(A[k:]) == sum(B[:k]) == sum(B[k:]):
    #         return k
    # return 0

    # prefix sum - fast
    aleft = [0] * n
    aright = [0] * n
    bleft = [0] * n
    bright = [0] * n

    # left sum -> 0-(k-1)
    for i in range(1, n):
        aleft[i] = aleft[i - 1] + A[i - 1]
        bleft[i] = bleft[i - 1] + B[i - 1]

    # right sum -> k to n-1
    aright[-1] = A[-1]
    bright[-1] = B[-1]
    for i in range(n - 2, -1, -1):
        aright[i] = A[i] + aright[i + 1]
        bright[i] = B[i] + bright[i + 1]

    print(f"a={A}, b={B}")
    print(f"aleft={aleft}, aright={aright}, bleft={bleft}, bright={bright}")
    for i in range(1, n - 1):
        if aleft[i] == aright[i] == bleft[i] == bright[i]:
            return i

    return -1


if __name__ == "__main__":

    iplist = [
        ["co", "dil", "ity"],
        ["abc", "yyy", "def", "csv"],
        ["potato", "kayak", "banana", "racecar"],
        ["eva", "jqw", "tyn", "jan"],
    ]
    for ip in iplist:
        print(
            f"A={ip}, get_longest_concatenated_str_with_unique_letters={get_longest_concatenated_str_with_unique_letters(ip)}"
        )

    print("***************************")
    iplist = [[1, 3, 6, 4, 1, 2], [1, 2, 3], [-1, -3]]
    for ip in iplist:
        print(f"ip={ip}, return_max_int={return_max_int(ip)}")

    print("***************************")
    for a, b, result in [
        ([4, -1, 0, 3], [-2, 5, 0, 3], 2),
        ([2, -2, -3, 3], [0, 0, 4, -4], 2),
        ([4, -1, -0, 3], [-2, 6, 0, 4], -1),
        ([1, 4, 2, -2, 5], [7, -2, -2, 2, 5], 2),
    ]:
        print(f"A={a}, B={b}, result={result}, get_fair_index={get_fair_index(a, b)}")
