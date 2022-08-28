from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current_position = 1
        current_node = head
        start = head
        while current_position < left:
            start = current_node
            current_node = current_node.next
            current_position += 1
        tail = current_node
        new_list = None
        while current_position >= left and current_position <= right:
            next_value = current_node.next
            current_node.next = new_list
            new_list = current_node