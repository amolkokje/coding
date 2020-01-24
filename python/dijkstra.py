import sys, os, copy
import heapq


# DIJKSTRA - for graph with weighted edges, find the shortest distance to all nodes from a given start node
# e.g. Networking - find the shortest distance to a server (distance between routers is a weight)

def dijkstra(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}  # or use sys.maxint to indicate some max value
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    visited = list()  # store all the visited nodes

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # visit the node only if not already visited
        if not current_vertex in visited:
            visited.append(current_vertex)

            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight

                # Only consider this new path if it's better than any path we've
                # already found.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance  # update the new distance, if it is lower
                    heapq.heappush(pq, (distance, neighbor))  # update the priority queue with new weight/distance

    return distances


# For a graph with no weights, BFS is the fastest way to find the shortest distance between 2 nodes
# DFS:
# -> Pre, In, Post order -> used mainly for tree traversal or in an array to try combinations.
# -> DFS takes less memory than BFS
# BFS:
# -> For finding shortest distance between 2 points in a graph or a tree


def calculate_min_distance(graph, v1, v2):
    queue = [[v1]]  # store lists of paths
    visited = [v1]  # visited nodes

    while queue:
        curr_path = queue.pop(0)

        # get the last node of the path. Check the neighbors of this node
        last_node = curr_path[-1]

        # check all the neighbors to see if reached the end
        for neighbor in graph[last_node]:
            if neighbor == v2:
                # found the shortest path
                return curr_path + [neighbor]

            elif neighbor not in visited:
                queue.append(curr_path + [neighbor])
                visited.append(neighbor)


# REF: https://www.interviewcake.com/concept/java/dijkstras-algorithm
# REF: https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
if __name__ == '__main__':
    example_graph = {
        'U': {'V': 2, 'W': 5, 'X': 1},
        'V': {'U': 2, 'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'W': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1},
    }
    print(dijkstra(example_graph, 'X'))

    example_graph = {
        'Memphis': {'New Orleans': 3, 'Nashville': 15, 'Mobile': 7, 'Atlanta': 10},
        'New Orleans': {'Memphis': 3, 'Mobile': 3},
        'Mobile': {'New Orleans': 3, 'Memphis': 7, 'Atlanta': 2, 'Savannah': 6},
        'Savannah': {'Mobile': 6, 'Atlanta': 1},
        'Atlanta': {'Savannah': 1, 'Mobile': 2, 'Memphis': 10, 'Nashville': 2},
        'Nashville': {'Memphis': 15, 'Atlanta': 2}
    }
    print(dijkstra(example_graph, 'Memphis'))

    print '********************'

    example_graph = {
        'U': ['V', 'W', 'X'],
        'V': ['U', 'X', 'W'],
        'W': ['V', 'U', 'X', 'Y', 'Z'],
        'X': ['U', 'V', 'W', 'Y'],
        'Y': ['X', 'W', 'Z'],
        'Z': ['W', 'Y'],
    }
    print(calculate_min_distance(example_graph, 'U', 'Z'))
    print(calculate_min_distance(example_graph, 'V', 'Y'))
