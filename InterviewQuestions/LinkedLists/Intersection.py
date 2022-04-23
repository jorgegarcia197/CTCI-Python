from operator import le


class NodeList():
    """ This represents a single node of a singly linked list"""

    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value


def Intersection(ListA: NodeList, ListB: NodeList):
    lenA = get_length(ListA)
    lenB = get_length(ListB)

    if lenA > lenB:
        diff = lenA-lenB
        NodeA = TraverseTo(ListA, diff)
    else:
        diff = lenB - lenA
        NodeB = TraverseTo(ListB, diff)

    ListA = NodeA if NodeA else ListA
    ListB = NodeB if NodeB else ListB

    while ListA != ListB:
        ListA = ListA.next
        ListB = ListB.next
    if not ListA:
        return None
    else:
        return ListA


def get_length(list: NodeList):
    counter = 0
    while list:
        counter += 1
        list = list.next
    return counter


def TraverseTo(list: NodeList, index):
    counter = 0
    while counter != index:
        list = list.next
        counter += 1
    return list
