# Given a directed graph and two nodes (S and E ) design an algorithm to fint out whether there is a route from S to E

# What I would do is a DFS and check by nodes if S node is adjacent to E

# First, I think i need to traverse to the nodes to find S and whenever I hit S, check the adjacency list and look for E, if not, return False


from gettext import find
from typing import List

graph = [[1, 2],
         [2, 1], [2, 8], [8, 2], [2, 3],
         [3, 5], [3, 6],
         [5, 10],
         [10, 5],
         [5, 15],
         [15, 5],
         [6, 12],
         [12, 6]]


def adj_list(graph):
    adj_list = {graph[i][0]: [] for i in range(len(graph))}
    for pair in graph:
        adj_list[pair[0]].append(pair[1])
    return adj_list


def findRoute(graph, start, end):
    visited = []
    adj_dict = adj_list(graph)
    return dfs(adj_dict, visited, start, end)


def dfs(graph, visited, current, end):
    if current == end:
        return True
    for neighbor in graph[current]:
        if neighbor in visited:
            continue
        visited.append(neighbor)
        if dfs(graph, visited, neighbor, end):
            return True
    return False


if __name__ == "__main__":
    # adj_dict = {1: [2], 2: [8, 3], 3: [5, 6], 5: [
    #     10, 15], 6: [12], 10: [], 15: [], 12: []}
    # adj_dict = {1: [2, 3], 2: [3, 5, 6], 3: [1], 5: [], 6: [7], 7: []}

    print(findRoute(graph, 5, 8))
