# Delete middle Node Problem

# This problem is a tricky one because we only have acces to the node we want to delete, because of that we only need to return True or False whether it can be done or not

# We just grab the next value node and replace the value we want to delete and link the value to the next.next Node
# In a nutshell, a shifting of nodes to the left



class NodeList():
    """ This represents a single node of a singly linked list"""

    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value


def delete_node(to_delete_node: NodeList)-> bool:
    if to_delete_node is None or to_delete_node.next is None:
        return False
    next_value = to_delete_node.next
    to_delete_node.value = next_value.value
    to_delete_node.next = next_value.next
    return True