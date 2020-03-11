import os, sys

# REF: https://www.facebook.com/careers/life/sample_interview_questions

"""
Find the pattern and complete the function:
int[][] spiral(int n);
where n is the size of the 2D array.

input = 3
123
894
765

input = 4
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07

input = 8
1 2 3 4 5 6 7 8
28 29 30 31 32 33 34 9
27 48 49 50 51 52 35 10
26 47 60 61 62 53 36 11
25 46 59 64 63 54 37 12
24 45 58 57 56 55 38 13
23 44 43 42 41 40 39 14
22 21 20 19 18 17 16 15
"""


# Solution: Keep going until need to turn and then turn right

def spiral(n):
    grid = [[-1 for _ in range(n)] for _ in range(n)]

    c = 1  # count
    x = y = 0  # start co-ordinates
    curr_move = 'right'  # starting direction to go in

    total = n * n  # total number of cells

    while True:
        # set value of point, and proceed
        grid[x][y] = c
        c += 1

        # select the direction to go based on the place where located

        if curr_move == 'right':
            if y + 1 < n and grid[x][y + 1] == -1:
                y += 1  # continue right
            else:
                curr_move = 'down'
                x += 1  # go down

        elif curr_move == 'down':
            if x + 1 < n and grid[x + 1][y] == -1:
                x += 1  # continue down
            else:
                curr_move = 'left'
                y -= 1  # go left

        elif curr_move == 'left':
            if y - 1 >= 0 and grid[x][y - 1] == -1:
                y -= 1  # continue left
            else:
                curr_move = 'up'  # go up
                x -= 1

        elif curr_move == 'up':
            if x - 1 >= 0 and grid[x - 1][y] == -1:
                x -= 1  # continue up
            else:
                curr_move = 'right'  # go right
                y += 1

        # if all points are done, then return
        if c > total:
            return grid


"""
Write a function that returns whether two words are exactly "one edit" away using the following signature:
bool OneEditApart(string s1, string s2);
An edit is:
- Inserting one character anywhere in the word (including at the beginning and end)
- Removing one character
- Replacing one character
"""


# review FB method, but does not seem very intuitive

def one_edit_apart(w1, w2):
    l1 = len(w1)
    l2 = len(w2)

    if (w1 == w2) or (l1 - l2 >= 2):
        return False

    # ensure that w1 is always shorter string
    if l1 > l2:
        w1, w2 = w2, w1
        l1, l2 = l2, l1

    i = 0
    while i<l1:
        if w1[i] != w2[i]:
            if l1 < l2:
                # remove possible?
                return w1==w2[:i]+w2[i+1:]
            elif l1 == l2:
                # replace possible?
                return w1[:i]+w1[i+1:] == w2[:i]+w2[i+1:]
        i+=1
    # reached at a point where only 1 extra char left in w2, and till here all chars in w1 are same as w2
    return True


"""
Queue using 2 stacks
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT

class Stack(object):
    def __init__(self):
        self.elements = list()

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop(0)

    def peek(self):
        return self.elements[0]

    def size(self):
        return len(self.elements)


class Queue(object):
    def __init__(self):
        self.s1 = Stack()  # to take in input
        self.s2 = Stack()  # to give out output

    def enqueue(self, x):
        self.s1.push(x)

    def dequeue(self):
        # transfer all from s1 to s2
        while self.s1.size() > 0:
            self.s2.push(self.s1.pop())

        # read last element from s2
        ret = self.s2.pop()

        while self.s2.size() > 0:
            self.s1.push(self.s2.pop())

        return ret

    def peek(self):
        while self.s1.size() > 0:
            self.s2.push(self.s1.pop())

        ret = self.s2.peek()

        while self.s2.size() > 0:
            self.s1.push(self.s2.pop())

        return ret


"""
https://algorithms.tutorialhorizon.com/colorful-numbers/

Objective: Given a number, find out whether its colorful or not.

Colorful Number: When in a given number, product of every digit of a sub-sequence are different. 
That number is called Colorful Number. 

Given Number : 3245
Output : Colorful
Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
this number is a colorful number, since product of every digit of a sub-sequence are different.
That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

Given Number : 326
Output : Not Colorful.
326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12
"""


def is_colorful(num):
    nums = [int(n) for n in str(num)]
    n = len(nums)

    multiples = list()

    for w in range(1, n):
        for j in range(n - w + 1):
            sub_nums = nums[j:j + w]

            multiply_out = reduce(lambda x, y: x * y, sub_nums)
            print 'sub={}, out={}'.format(sub_nums, multiply_out)
            if multiply_out in multiples:
                return False
            multiples.append(multiply_out)
    return True


if __name__ == '__main__':

    print '##########################################'
    for num in [3245, 326]:
        print 'num={}, is_colorful={}'.format(num, is_colorful(num))

    print '##########################################'
    for n in [3, 4]:
        print 'n={}, grid={}'.format(n, spiral(n))

    print '##########################################'
    for words in [
        ('cat', 'dog'),
        ('cat', 'cats'),
        ('cat', 'cut'),
        ('cat', 'cast'),
        ('cat', 'at'),
        ('cat', 'act')
    ]:
        print '{}, {}, one_edit_apart={}'.format(words[0], words[1], one_edit_apart(words[0], words[1]))
    sys.exit()

    print '##########################################'
    q = Queue()
    print 'Enqueue ...'
    for i in range(10):
        q.enqueue(i)

    print 'Dequeue ...'
    for _ in range(10):
        print q.dequeue()
