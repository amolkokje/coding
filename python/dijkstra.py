import sys, os, copy
import heapq


# DIJKSTRA - for graph with weighted edges, find the shortest distance to all nodes from a given start node
# e.g. Networking - find the shortest distance to a server (distance between routers is a weight)

# By using a priority queue, we ensure that as we explore one vertex after another, we are always exploring
# the one with the smallest distance.

# NOTE:
# - No weight on edges --> normal queue
# - Weights on edges --> priority queue
import math


# BFS - minheap
# NOTE: graph is undirected, so track already visited nodes to avoid forever looping
def dijkstra(graph, start):
    result = {node: math.inf for node in graph.keys()}
    result[start] = 0

    visited = set()
    minheap = [(0, start)]

    while len(minheap) > 0:
        distance, node = heapq.heappop(minheap)

        if node in visited:
            continue
        visited.add(node)

        for n, ndistance in graph[node].items():
            # calculate the distance from start to the neighbor
            current_distance = distance + ndistance
            #  update min distance to the neighbor node
            if current_distance < result[n]:
                result[n] = current_distance
                heapq.heappush(minheap, (current_distance, n))

    return result


# For shortest distance search with weighted edges, problem with BFS is that it will return the first found, which
# may not be shortest. So, for this case, need to find all the possibilities and then pick the lowest cost path
# Hence, use DFS -OR- use Dijkstra and get the value you want from it
def calculate_min_distance_weighted(graph, v1, v2):
    def _recurse(n, path, wformed):
        if n in path:
            return

        if n == v2:
            return wformed

        mind = None
        for neigh in graph[n].keys():
            w = _recurse(neigh, path + [n], wformed + graph[n][neigh])
            if w:
                if not mind:
                    mind = w
                elif w < mind:
                    mind = w

        return mind

    return _recurse(v1, [], 0)


# weighted graph
# calculate: min distance between 2 nodes
def calculate_min_distance_weighted_new(graph, v1, v2):
    minheap = [(0, v1)]

    visited = set()
    while len(minheap) > 0:
        distance, node = heapq.heappop(minheap)

        if node in visited:
            continue
        visited.add(node)

        for neighbor, ndistance in graph[node].items():
            if neighbor == v2:
                return distance + ndistance

            heapq.heappush(minheap, (distance + ndistance, neighbor))


# For a graph with no weights, BFS is the fastest way to find the shortest distance between 2 nodes
# DFS:
# -> Pre, In, Post order -> used mainly for tree traversal or in an array to try combinations.
# -> DFS takes less memory than BFS
# BFS:
# -> For finding shortest distance between 2 points in a graph or a tree


# BFS works very well for non-weighted shortest distance search
def find_shortest_path(graph, v1, v2):
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
if __name__ == "__main__":
    example_graph = {
        "U": {"V": 2, "W": 5, "X": 1},
        "V": {"U": 2, "X": 2, "W": 3},
        "W": {"V": 3, "U": 5, "X": 3, "Y": 1, "Z": 5},
        "X": {"U": 1, "V": 2, "W": 3, "Y": 1},
        "Y": {"X": 1, "W": 1, "Z": 1},
        "Z": {"W": 5, "Y": 1},
    }
    print(calculate_min_distance_weighted(example_graph, "X", "U"))
    print(calculate_min_distance_weighted_new(example_graph, "X", "U"))
    print(dijkstra(example_graph, "X"))

    example_graph = {
        "Memphis": {"New Orleans": 3, "Nashville": 15, "Mobile": 7, "Atlanta": 10},
        "New Orleans": {"Memphis": 3, "Mobile": 3},
        "Mobile": {"New Orleans": 3, "Memphis": 7, "Atlanta": 2, "Savannah": 6},
        "Savannah": {"Mobile": 6, "Atlanta": 1},
        "Atlanta": {"Savannah": 1, "Mobile": 2, "Memphis": 10, "Nashville": 2},
        "Nashville": {"Memphis": 15, "Atlanta": 2},
    }
    print(dijkstra(example_graph, "Memphis"))

    example_graph = {
        "U": ["V", "W", "X"],
        "V": ["U", "X", "W"],
        "W": ["V", "U", "X", "Y", "Z"],
        "X": ["U", "V", "W", "Y"],
        "Y": ["X", "W", "Z"],
        "Z": ["W", "Y"],
    }
    print(find_shortest_path(example_graph, "U", "Z"))
    print(find_shortest_path(example_graph, "V", "Y"))
