from collections import deque
projects = ["a", "b", "c", "d", "e", "f", "g"]
dependencies = [
    ("d", "g"),
    ("a", "e"),
    ("b", "e"),
    ("c", "a"),
    ("f", "a"),
    ("b", "a"),
    ("f", "c"),
    ("f", "b"),
]


def adj_list(graph, projects):
    values = []
    adj_dict = {p: [] for p in projects}
    for pair in graph:
        adj_dict[pair[0]].append(pair[1])
        if pair[1] not in values:
            values.append(pair[1])
    return adj_dict, values


def Diff(li1, li2):
    return list(set(li1) ^ set(li2))


def buildOrder(adj_dict, values):
    output = []
    queue = deque(values)
    while len(queue) > 0:
        currentNode = queue.popleft()
        if currentNode not in output:
            output.append(currentNode)
        connections = adj_dict[currentNode]
        for connection in connections:
            queue.append(connection)
    return output if output else False


if __name__ == "__main__":
    adj_dict, values = adj_list(dependencies, projects)
    print(adj_dict)
    print(Diff(values, projects))
    print(buildOrder(adj_dict, Diff(values, projects)))
