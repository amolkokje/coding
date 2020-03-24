"""
Select k-th largest element?
list = [ 3,6,2,18,29,4,5 ]
k=1, return 18,
k=0, return 29

-> time complexity
-> space complexity
"""
import heapq


def select_kth_largest(iplist, k):
    """
    APPROACH-1:
    - sort the list - N.logN
    - pop elements until get - K
    - Complexity: N.logN + K

    APPROACH-2:
    - store all in maxheap - N(no of elements)*logN(heapify operation)
    - pop elements until get - K
    - Complexity: N.logN + K

    APPROACH-3: (best)
    - store largest K elements in minheap - N.logK
    - if element is found greater than root, then pop the min, and put the element in the heap
    - at end, return the root of heap
    - Complexity: N.logK
    """
    minheap = list()

    for ele in iplist:
        # print minheap, k
        if len(minheap) > k:  # store k+1 elements in the heap, instead of k
            if ele > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, ele)
        else:
            heapq.heappush(minheap, ele)
    return minheap[0]


"""
Merge Ranges
input: 
[ (2,4), (5,6), (7,9.2) ]
[ (3,3.4), (4.2,4.6), (5.5,7) ]

<------------------------------------------->
    |--------|    |----|    |---------|
    2        4    5    6    7         9.2
        |--|   |-|   |------|
        3,3.4 4.2,4.6   5.5,7 

output:
[ (2,4), (4.2,4.6), (5.5,7) ]

Q: How many total comparisons?
"""


def merge_ranges(ranges1, ranges2):
    """
    APPROACH-1:
    - add range1
    - go through each entry in range2, if found in range then skip, and if not, extend the range
    """

    def _pt_exists_in_range(value, r):
        return True if r[0] <= value <= r[1] else False

    def _merge_range(r):
        """ helper to merge input with range1 """
        start, end = r
        for r1 in ranges1:
            start_exists = _pt_exists_in_range(start, r1)
            end_exists = _pt_exists_in_range(end, r1)
            if start_exists and end_exists:
                return  # both exist in the range, no action required
            elif start_exists and not end_exists:
                r1[1] = end  # only start exists in the range -> stretch the end of this range
                return
            elif not start_exists and end_exists:
                r1[0] = start  # only end exists in the range -> stretch the start of this range
                return

        # if the start/end does not exist in any range, add the new range in
        # IMPORVEMENT - instead of adding that range at the end, it can be added in the right order using a helper method
        ranges1.append([start, end])

    for r2 in ranges2:
        _merge_range(r2)


"""
Q: For words in the list 'words', return if this list is sorted lexically as per the list 'alphabet' instead of a->z

INPUT:
words = [ 'cbt' , 'cat', 'bat', 'tab' ] --> words can have different length
alphabet = [ 'c', 'b', 'a', 't' ]  --> no repeats in this list

OUTPUT: 
True

e.g. 
cat, catb -> True
catb, cat -> False
ccc, ccc -> True
"""


def is_sorted(words, alphabets):
    # store all alphabets in a dict for easy checking
    alphadict = dict()
    for k in range(len(alphabets)):
        alphadict[alphabets[k]] = k

    def _is_word_greater_than(word1, word2):
        """
        validate if word1 > word2
        """
        # print word1, word2
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1, n2)
        for i in range(n):
            if alphadict[word1[i]] < alphadict[word2[i]]:
                return True

        if n1 > n2:  # Case: catb, cat -> False
            return False

        return True  # Case: n1==n2, n2>n1

    for i in range(1, len(words) - 1):
        # print i
        if not _is_word_greater_than(words[i], words[i + 1]):
            return False

    return True


"""
Q: Find a way to store the vectors in a memory efficient way to be able to calculate the dot product.
- Calculate the dot product.
- Input vectors can be small/large and may be input as sparse vectors

Dot Product:
A = (1,2,1)
B = (2,0,0)
A.B = 1*2 + 2*0 + 1*0 = 2

Sparse Vector: many zeroes between numbers in a vector
A = (...0, 1, 0...0, 2, 0...0, 1, 0...0, 3, 4, 0...)
"""


def compress_vector(arr):
    """ generates list of tuples such that (count of zeros before, number) from a sparse vector """
    n = len(arr)
    i = 0
    compressed = list()

    while i < n:
        # print '-----> i={}'.format(i)
        if arr[i] == 0:
            j = i + 1
            c = 1
            while j < n:
                # print 'j={}'.format(j)
                if arr[j] != 0:
                    compressed.append((c, arr[j]))
                    i += c
                    break
                c += 1
                j += 1
        else:
            compressed.append((0, arr[i]))
        i += 1

    return compressed


def decompress_vector(x):
    """ returns decompressed tuple one by one as generator is accessed -> Avoids loading all in memory """
    for tup in x:
        yield [0] * tup[0] + [tup[1]]


def dot_product(a, b):
    """ calculates dot products of 2 input sparse vectors """

    # get genearators for lazy loading of decompressed vectors
    ad = decompress_vector(a)
    bd = decompress_vector(b)

    abuffer = list()
    bbuffer = list()
    out = list()
    while True:
        # until there are no more in the vectors, keep getting them
        try:
            if not abuffer:
                abuffer += next(ad)
            if not bbuffer:
                bbuffer += next(bd)
        except StopIteration:
            # when the generator ends and you can no longer call next() on it, and it raises StopIteration exception
            break

        if abuffer and bbuffer:
            n = min(len(abuffer), len(bbuffer))
            # as you calculate the dot product, drop the elements
            for _ in range(n):
                out.append(abuffer.pop(0) * bbuffer.pop(0))
        else:
            break

    print 'OUT=[{}]'.format(out)
    return compress_vector(out)


"""
Q: Connect Levels of binary tree
          1                   1 -> 
        /   \                 2 -> 5 -> 
       2     5                3 -> 4 -> 6 ->  
      / \     \
     3   4     6 
"""


def reconnect_tree(root):
    """
    APPROACH:
    - at each level store the last node
    - if last node exists, update the next value of the node
    - if it does not exist, add last node

    Note:
    - Earlier stored the list at each level, but the space complexity in that case would have been N (number of nodes in the tree)
    - Optimization store only last node which makes space complexity M(no of levels)
    """
    last_nodes = list()  # list to store last node at each level

    def _recurse(node, level):
        if node:
            if len(last_nodes) > level:
                # if last node for a particular level exists, update its next_node property, and also update node in
                # the list
                last_node = last_nodes[level]
                last_node.next_node = node
                last_nodes[level] = node
            else:
                # if last_nodes list does not have last node for a particular level, add it
                last_nodes.append(node)

            _recurse(node.left, level + 1)
            _recurse(node.right, level + 1)

    _recurse(root, 0)


"""
PRODUCT DESIGN: contest system for leetcode
"""

if __name__ == '__main__':

    print '***********************'
    iplist = [3, 6, 2, 18, 29, 4, 5]
    for k in [0, 1]:
        print 'iplist=[{}], k=[{}], kth-largest=[{}]'.format(iplist, k, select_kth_largest(iplist, k))

    print '***********************'
    words = ['cbt', 'cat', 'bat', 'tab']
    alphabets = ['c', 'b', 'a', 't']
    print 'words=[{}], alphabets=[{}], is-sorted=[{}]'.format(words, alphabets, is_sorted(words, alphabets))

    print '***********************'
    ranges1 = [[2, 4], [5, 6], [7, 9.2]]
    ranges2 = [[3, 3.4], [4.2, 4.6], [5.5, 7]]
    print 'ranges1=[{}], ranges2=[{}]'.format(ranges1, ranges2)
    merge_ranges(ranges1, ranges2)
    print 'merged-ranges=[{}]'.format(ranges1)

    print '***********************'
    a = [0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 4, 5, 6, 0, 0, 0, 0, 7]
    b = [0, 0, 0, 3, 2, 0, 0, 1, 0, 3, 0, 0, 0, 0, 4, 5, 6, 0, 0, 0, 0, 7]
    # out:[0,0,0,0,4, 0,0,0,0,9, 0,0,0,0,16, 25, 36, 0,0,0,0,49 ] -> [ (4,4), (4,9), (4,16), (0,25), (0,36), (4,7) ]
    print 'a=[{}], b=[{}]'.format(a, b)
    a = compress_vector(a)
    b = compress_vector(b)
    print 'COMPRESSED: a=[{}], b=[{}]'.format(a, b)
    print 'Dot Product = [{}]'.format(dot_product(a, b))
