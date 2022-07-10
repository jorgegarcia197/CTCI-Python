from collections import deque
from this import s

#! Incorrect


def djikstras(edges, start):
    """perform djikstras algorithmm

    Args:
        edges (list): _description_
        start (int): _description_
    """

    min_dist = [float("inf")] * len(edges)
    queue = deque()
    queue.append(edges[start][0])
    min_dist[start] = 0
    currentEdge = start
    visited = set()

    while len(queue) > 0:
        counter = 0
        length_at_start = len(queue)
        while counter < length_at_start:
            destination, distance = queue.popleft()
            total_distance = min_dist[currentEdge] + distance
            if total_distance < min_dist[destination]:
                min_dist[destination] = total_distance
                currentEdge = destination
            if edges[destination] != None:
                for edge in edges[destination]:
                    queue.append(edge)
            counter += 1
    for i in range(len(min_dist)):
        if min_dist[i] == float("inf"):
            min_dist[i] = -1
    return min_dist


def djikstras_recursive(edges, start):
    """perform djikstras algorithmm

    Args:
        edges (list): _description_
        start (int): _description_
    """
    number_of_vertices = len(edges)
    min_dist = [float("inf")] * len(edges)
    min_dist[start] = 0
    visited = set()

    while len(visited) < number_of_vertices:
        vertex, min_distance = get_min_dist(edges, min_dist, visited)

        if min_distance == float("inf"):
            break
        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distance = edge
            if destination in visited:
                continue
            total_dist = min_distance + distance
            if total_dist < min_dist[destination]:
                min_dist[destination] = total_dist
    for i in range(len(min_dist)):
        if min_dist[i] == float("inf"):
            min_dist[i] = -1
    return min_dist


def get_min_dist(edge, min_dist, visited):
    currentMinDist = float("inf")
    vertex = -1

    for idx, distance in enumerate(min_dist):
        if distance < currentMinDist and idx not in visited:
            currentMinDist = distance
            vertex = idx

    return vertex, currentMinDist


if __name__ == "__main__":
    edges = [
        [
            [1, 7]
        ],
        [
            [2, 6],
            [3, 20],
            [4, 3]
        ],
        [
            [3, 14]
        ],
        [
            [4, 2]
        ],
        [],
        []
    ]
    start = 0
    print(djikstras_recursive(edges, start))
