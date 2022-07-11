def cycleInGraph(edges):
    # Write your code here.
    visited = []
    return detect_cycle(0, edges, visited)


def detect_cycle(starting, graph, visited):
    neighbours = graph[starting]
    if not neighbours:
        return False
    for neighbour in neighbours:
        if neighbour in visited:
            return True
        visited.append(neighbour)
        return detect_cycle(neighbour, graph, visited)


def isCyclicUtil(graph, v, visited, recStack):

    # Mark current node as visited and
    # adds to recursion stack
    visited[v] = True
    recStack[v] = True

    # Recur for all neighbours
    # if any neighbour is visited and in
    # recStack then graph is cyclic
    for neighbour in graph[v]:
        if visited[neighbour] == False:
            if isCyclicUtil(edges, neighbour, visited, recStack) == True:
                return True
        elif recStack[neighbour] == True:
            return True

    # The node needs to be popped from
    # recursion stack before function ends
    recStack[v] = False
    return False

    # Returns true if graph is cyclic else false


def isCyclic(edges):
    visited = [False] * (len(edges) + 1)
    recStack = [False] * (len(edges) + 1)
    for node in range(len(edges)):
        if visited[node] == False:
            if isCyclicUtil(edges, node, visited, recStack) == True:
                return True
    return False


if __name__ == "__main__":
    edges = [
        [1],
        [2, 3, 4, 5, 6, 7],
        [],
        [2, 7],
        [5],
        [],
        [4],
        [0]
    ]
    print(isCyclic(edges))
