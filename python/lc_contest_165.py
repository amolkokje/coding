"""
https://leetcode.com/contest/weekly-contest-165/problems/count-square-submatrices-with-all-ones/
"""


class Solution(object):
    def is_all_one(self, square):
        # print square
        n = len(square)
        for i in range(n):
            for j in range(n):
                # print i,j
                if square[i][j] != 1:
                    return False
        return True

    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)  # rows
        n = len(matrix[0])  # cols
        print 'm={}, n={}'.format(m, n)

        count = 0
        max_sides = min(m, n)
        for side in range(1, max_sides + 1):
            # in a row
            for i in range(m - side + 1):
                # in a col
                for j in range(n - side + 1):

                    # generate square
                    square = list()
                    for x in range(i, i + side):
                        square.append(matrix[x][j:j + side])

                    if self.is_all_one(square):
                        count += 1
                        # print '** count={}'.format(count)

        return count


"""
https://leetcode.com/contest/weekly-contest-165/problems/find-winner-on-a-tic-tac-toe-game/
"""


class Solution(object):
    def has_winner(self, board):
        print '*** BOARD = {}'.format(board)
        n = len(board)

        def _all_same(arr):
            i = 1
            m = len(arr)
            while i < m:
                if arr[i] == '' or arr[i] != arr[i - 1]:
                    return False
                i += 1
            return True

        for i in range(n):
            if _all_same(board[i]) or _all_same([board[j][i] for j in range(n)]):
                return True

        if _all_same([board[i][i] for i in range(n)]) or _all_same([board[i][n - 1 - i] for i in range(n)]):
            return True

        return False

    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        c = 0
        board = [['' for _ in range(3)] for _ in range(3)]
        move_a = False
        for move in moves:
            c += 1
            move_a = not move_a
            if move_a:
                board[move[0]][move[1]] = 'A'
            else:
                board[move[0]][move[1]] = 'B'

            if c > 3:
                if self.has_winner(board):
                    if move_a:
                        return 'A'
                    else:
                        return 'B'

        if c >= 9:
            return 'Draw'
        return 'Pending'


"""
https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
"""


class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """

        def _recurse(total_jumbo, total_small, tomato, cheese):
            if tomato == 0 and cheese == 0:
                return [total_jumbo, total_small]

            if tomato >= 2 and cheese >= 1:
                found = _recurse(total_jumbo, total_small + 1, tomato - 2, cheese - 1)
                if found:
                    return found

            if tomato >= 4 and cheese >= 1:
                found = _recurse(total_jumbo + 1, total_small, tomato - 4, cheese - 1)
                if found:
                    return found

        return _recurse(0, 0, tomatoSlices, cheeseSlices)
