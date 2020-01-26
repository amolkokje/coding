import sys, os, copy


# Traveling Salesman Problem: (NP complete)
# Given a set of cities and distance between every pair of cities, the problem is to find the shortest possible
# route that visits every city exactly once and returns back to the starting point.
# https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/

def get_shortest_distance_to_visit_all_cities(grid, start_city):
    path_distance_tuples = list()
    n = len(grid)  # total cities
    print 'start_city={}'.format(start_city)

    def get_connections(x):
        connections_dict = dict()
        for i in range(n):
            if grid[x][i] != 0:
                connections_dict[i] = grid[x][i]
        return connections_dict

    def _recurse(visited, i, distance):
        if i in visited:
            return

        visited_local = copy.deepcopy(visited)
        visited_local.append(i)
        #print 'VISITED={}'.format(visited_local)

        conn_dict = get_connections(i)

        if len(visited_local) == n:
            # visited all
            # if start in neighbors, made it
            if start_city in conn_dict.keys():
                path_distance_tuples.append((visited_local + [start_city], distance + grid[i][start_city]))
                #return (visited_local + [start_city], distance + grid[i][start_city])  # IF REQUIRED TO FIND A PATH
            else:
                return
        else:
            # continue recursing

            for conn in conn_dict.keys():
                _recurse(visited_local, conn, distance + grid[i][conn])
                # IF NEED TO FIND ALL PATHS
                #found = _recurse(visited_local, conn, distance + grid[i][conn])
                #if found:
                #    return found

    _recurse(list(), start_city, 0)
    paths_sorted_by_distance = sorted(path_distance_tuples, key=lambda x: x[1])
    print 'Paths sorted by distance={}'.format(paths_sorted_by_distance)
    return paths_sorted_by_distance[0][1]


# Hamiltonian Cycle: (NP Complete)
# Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once. A Hamiltonian cycle
# (or Hamiltonian circuit) is a Hamiltonian Path such that there is an edge (in the graph) from the last vertex to the
# first vertex of the Hamiltonian Path. Determine whether a given graph contains Hamiltonian Cycle or not. If it
# contains, then prints the path. Following are the input and output of the required function.
# https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/

def hamilton_cycle_exists(grid):
    n = len(grid)  # total pts
    start = 0
    visited = [False for _ in range(n)]
    print 'n={}'.format(n)

    def get_connections(x):
        connections = list()
        for i in range(n):
            if grid[x][i] == 1:
                connections.append(i)
        return connections

    def _recurse(visited, i, path):
        if visited[i]:
            return

        visited_all = False
        visited_local = copy.deepcopy(visited)
        visited_local[i] = True

        path_local = copy.deepcopy(path)
        path_local.append(i)

        # print 'VISITED={}, PATH={}'.format(visited_local, path_local)
        # print filter(lambda x: x==True, visited_local)

        if len(filter(lambda x: x == True, visited_local)) == n:
            # if can go to 'start' from here, then hamilton cycle/path exists
            visited_all = True

        connections = get_connections(i)
        # print connections, visited_all
        if visited_all:
            if start in connections:
                # print 'PATH={}'.format(path_local + [start])
                return True
            else:
                return False
        else:
            # keep looking
            for conn in connections:
                # return the first found, and no need to recurse further
                found = _recurse(visited_local, conn, path_local)
                if found:
                    return found
            return False

    return _recurse(visited, start, list())


# N-Queen Problem:
# The N Queen is the problem of placing N chess queens on an NxN chessboard so that no two queens attack each other.
# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

def place_n_queens(n):
    # n - number of row/cols = no of queens

    board = [[False for _ in range(n)] for _ in range(n)]

    # put the first queen at a random location - 2nd row
    board[2][0] = True

    # need to check only cols on left hand side, as right not filled yet
    def is_cell_ok(row, col):
        # ensure there is none in the same row
        if True in board[row]:
            return False

        # check left-up diagonal
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1

        # check left-down diagonal
        i = row
        j = col
        while i < n and j >= 0:
            if board[i][j]:
                return False
            i += 1
            j -= 1

        # check right-up diagonal
        i = row
        j = col
        while i >= 0 and j < n:
            if board[i][j]:
                return False
            i -= 1
            j += 1

        # check right-down diagonal
        i = row
        j = col
        while i < n and j < n:
            if board[i][j]:
                return False
            i += 1
            j += 1

        return True

    # put a queen in each col one by one
    for i in range(1, n):

        # for each row, check if the cell is OK
        for k in range(n):
            if is_cell_ok(row=k, col=i):
                board[k][i] = True
                print 'Putting Queen: ({},{})'.format(k, i)
                break

    return board


# Graph Coloring: (NP Complete)
# https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/
# Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that no
# two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment
# of colors to all vertices.

def color_graph(grid, m):
    # grid - cost adjacency matrix
    # m - number of colors

    n = len(grid)  # number of cells
    possibilities = list()  # list of dicts {point: color}

    def _get_connections(p):
        conns = list()
        # in the same row, check which cols are 1
        for i in range(n):
            if grid[p][i] == 1:
                conns.append(i)
        return conns

    def _get_usable_colors(point_color_dict, conns):
        color_list = list()
        for conn in conns:
            if point_color_dict.get(conn) is not None:
                color_list.append(point_color_dict[conn])

        usable_colors = list()
        for i in range(m):
            if i not in color_list:
                usable_colors.append(i)

        return usable_colors

    def _recurse(p, pcolor_dict):
        visited = pcolor_dict.keys()
        if p in visited:
            return

        # SET COLOR OF POINT
        connections = _get_connections(p)

        # 2 levels of recursion
        # RECURSE-1: get list of colors which are not already taken by connections and recurse on them
        usable_colors = _get_usable_colors(pcolor_dict, connections)

        if not usable_colors:
            # all colors are taken by neighbors, no possibility
            return

        for color in usable_colors:
            # set current point to that color and recurse
            pcolor_dict_local = copy.deepcopy(pcolor_dict)
            pcolor_dict_local[p] = color

            # if all points are already colored, then found a possibility
            if len(pcolor_dict_local.keys()) == n:
                # possibilities.append(pcolor_dict_local)  # THIS IN CASE YOU WANT TO LIST ALL THE POSSIBILITIES
                return pcolor_dict_local  # THIS IS TO RETURN IF FOUND A POSSIBILITY

            # RECURSE-2: further, can recurse in direction of any connection
            for conn in connections:
                found = _recurse(conn, pcolor_dict_local)  # RETURN IF FOUND ALREADY FROM FIRST RECURSION
                if found:
                    return found

    # get the first point in the graph and start from there
    found = _recurse(0, dict())
    # return possibilities  # IF NEED TO RETURN ALL POSSIBILITIES
    if found:
        return found




if __name__ == '__main__':
    grid = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    m = 3
    print 'Color Graph = {}' .format(color_graph(grid, m))

    print '###############################################################'

    print 'Place N queens in NxN matrix = {}'.format(place_n_queens(4))

    print '###############################################################'

    grid = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print 'Shortest path to visit all cities = {}'.format(get_shortest_distance_to_visit_all_cities(grid, 1))

    print '###############################################################'

    # Hamilton: Undirected graph, with all weights as 1
    """
    (0)--(1)--(2)
     |   / \   |
     |  /   \  | 
     | /     \ |
    (3)-------(4)
    """

    grid = [  # grid -> distance/weight matrix
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ]
    print 'Hamilton Cycle Exists = {}'.format(hamilton_cycle_exists(grid))

    """
    (0)--(1)--(2)
     |   / \   |
     |  /   \  | 
     | /     \ |
    (3)       (4)
    """
    grid = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0]
    ]
    print 'Hamilton Cycle Exists = {}'.format(hamilton_cycle_exists(grid))
