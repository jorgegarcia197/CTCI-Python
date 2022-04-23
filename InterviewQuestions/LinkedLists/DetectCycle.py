class NodeList():
    """ This represents a single node of a singly linked list"""

    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value


def FindCycle(head: NodeList):
    hare = tortoise = head
    while True:
        hare = hare.next
        tortoise = tortoise.next
        if hare is None or hare.next is None:
            return False
        else:
            hare = hare.next
        if hare == tortoise:
            break
    meeting_point = hare
    p1 = head
    while p1 != meeting_point:
        p1 = p1.next
        meeting_point = meeting_point.next
    return p1

def FindCycle_with_list(head:NodeList):
    seen = []
    current = head
    if not head:
        return False
    while current:
        if current not in seen:
            seen.append(current)
        else:
            return True
        current = current.next
    return False
    


    