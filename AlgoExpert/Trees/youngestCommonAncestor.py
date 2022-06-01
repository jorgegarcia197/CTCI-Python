# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name, ancestor=None):
        self.name = name
        self.ancestor = ancestor


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    ancestorOneHeight = getHeightToTopAncestor(descendantOne, topAncestor)
    ancestorTwoHeight = getHeightToTopAncestor(descendantTwo, topAncestor)
    while ancestorOneHeight != ancestorTwoHeight:
        if ancestorOneHeight < ancestorTwoHeight:
            descendantTwo = descendantTwo.ancestor
            ancestorTwoHeight -= 1
        elif ancestorOneHeight > ancestorTwoHeight:
            descendantOne = descendantOne.ancestor
            ancestorOneHeight -= 1
    while descendantOne != descendantTwo and descendantOne != None and descendantTwo != None:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
    return descendantOne


def getHeightToTopAncestor(descendant, topAncestor):
    height = 0
    while descendant != topAncestor:
        height += 1
        descendant = descendant.ancestor
    return height


if __name__ == '__main__':
    input_date = {
        "nodes": [
            {"ancestor": None, "id": "A", "name": "A"},
            {"ancestor": "A", "id": "B", "name": "B"},
            {"ancestor": "A", "id": "C", "name": "C"},
            {"ancestor": "B", "id": "D", "name": "D"},
            {"ancestor": "B", "id": "E", "name": "E"},
            {"ancestor": "C", "id": "F", "name": "F"},
            {"ancestor": "C", "id": "G", "name": "G"},
            {"ancestor": "D", "id": "H", "name": "H"},
            {"ancestor": "D", "id": "I", "name": "I"}
        ]
    }
    nodes = [AncestralTree(node["name"], node["ancestor"])
             for node in input_date["nodes"]]

    print(getYoungestCommonAncestor(nodes[0], nodes[4], nodes[8]))
