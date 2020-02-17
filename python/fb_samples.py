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

    if l1 == l2:  # is replace possible?
        for i in range(l1):
            if w1[i] != w2[i]:
                if i + 1 < n:  # middle element
                    if w1 == w2[:i] + w1[i] + w2[i + 1:]:
                        return True
                    else:
                        return False
                else:  # end element
                    if w1 == w2[:i] + w2[i]:
                        return True
                    else:
                        return False

    elif l1 < l2:  # is remove possible?
        for i in range(l2):
            if i < l1:  # middle element
                if w1[i] != w2[i]:
                    if w1 == w2[:i] + w2[i + 1:]:
                        return True
                    else:
                        return False
            else:  # last element
                if w1 == w1[:i]:
                    return True
                else:
                    return False


if __name__ == '__main__':

    for n in [3, 4]:
        print 'n={}, grid={}'.format(n, spiral(n))

    for words in [
        ('cat', 'dog'),
        ('cat', 'cats'),
        ('cat', 'cut'),
        ('cat', 'cast'),
        ('cat', 'at'),
        ('cat', 'act')
    ]:
        print '{}, {}, one_edit_apart={}'.format(words[0], words[1], one_edit_apart(words[0], words[1]))
