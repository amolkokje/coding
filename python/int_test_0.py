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
    #print (ip_str)
    return True if len(ip_str) == len(list(set(ip_str))) else False

def get_longest_concatenated_str_with_unique_letters(A):
    n = len(A)
    visited = [ None for _ in range(n) ]
    str_with_unique_letters = list()

    def _recurse(str_formed, visited, i):
        if visited[i]:
            return

        visited_local = copy.deepcopy(visited)
        str_formed_local = copy.deepcopy(str_formed)

        visited_local[i] = True
        str_formed_local += A[i]

        if all_letters_distinct(str_formed_local):
            if str_formed_local not in str_with_unique_letters:
                str_with_unique_letters.append(str_formed_local)

            for j in range(i+1, n):
                _recurse(str_formed_local, visited_local, j)

    for i in range(n):
        _recurse('', visited, i)

    #print str_with_unique_letters
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
    for k in range(1,n-1):
        if sum(A[:k]) == sum(A[k:]) == sum(B[:k]) == sum(B[k:]):
            return k
    return 0



if __name__ == '__main__':

    iplist = [ [ 'co', 'dil', 'ity' ],
               [ 'abc', 'yyy', 'def', 'csv' ],
               [ 'potato', 'kayak', 'banana', 'racecar' ],
               [ 'eva', 'jqw', 'tyn', 'jan' ]]
    for ip in iplist:
        print 'A={}, get_longest_concatenated_str_with_unique_letters={}'.format(ip, get_longest_concatenated_str_with_unique_letters(ip))

    print '***************************'
    iplist = [ [1, 3, 6, 4, 1, 2], [1, 2, 3], [-1, -3] ]
    for ip in iplist:
        print 'ip={}, return_max_int={}'.format(ip, return_max_int(ip))

    print '***************************'
    iplist = [ ([4,-1,0,3], [-2,5,0,3]),
               ([2,-2,-3,3], [0,0,4,-4]),
               ([4,-1,-0,3], [-2,6,0,4]),
               ([1,4,2,-2,5],[7,-2,-2,2,5])]
    for ip in iplist:
        print 'A={}, B={}, get_fair_index={}'.format(ip[0], ip[1], get_fair_index(ip[0], ip[1]))