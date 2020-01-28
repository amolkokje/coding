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
        n = len(board)

        def _all_same(arr):
            xor = reduce(lambda x, y: x ^ y, arr)
            return True if xor == 0 else False

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
        n = 3
        max_moves = n * n
        moves_a = [[False for _ in range(n)] for _ in range(n)]
        moves_b = [[False for _ in range(n)] for _ in range(n)]

        c = 0
        total_moves = len(moves)
        for c in range(total_moves):
            move = moves[c]
            if c % 2 != 0:
                moves_b[move[0]][move[1]] = True
                if self.has_winner(moves_b):
                    return 'B'
            else:
                moves_a[move[0]][move[1]] = True
                if self.has_winner(moves_a):
                    return 'A'
            c += 1

        if c < max_moves - 1:
            return 'Pending'
        return 'Draw'


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
