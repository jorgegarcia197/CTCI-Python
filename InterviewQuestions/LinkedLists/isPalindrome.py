

class NodeList():
    """ This represents a single node of a singly linked list"""

    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value


def isPalindrome(head: NodeList) -> bool:
    """Determine whether the values of a linked list correspond to a palindrome

    Args:
        head (NodeList): The head value of the linked list

    Returns:
        bool: True if values represent a palindrome False otherwise
    """
    # slow and fast runner, with this method, the slow should always fit the middle part of the linked list
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    reversed_list = reverse(slow)
    list1 = head
    while list1 and reversed_list:
        if list1.value != reversed_list.value:
            return False
        list1 = list1.next
        reversed_list = reversed_list.next
    return True


# Helper function
def reverse(head):
    """Reverse a linked list in place

    Args:
        head (NodeList): The head value of the linked list to reverse

    Returns:
        NodeList: The new head value of the reversed linked list
    """
    current = head
    prev = None
    while current:
        next_value = current.next
        current.next = prev
        prev = current
        current = next_value
    head = prev
    return head


if __name__ == "__main__":
    palindrome_list = NodeList(1, NodeList(2, NodeList(2, NodeList(1))))
    print(isPalindrome(palindrome_list))
