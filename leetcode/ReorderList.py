from typing import List, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # ! head = [1,2,3,4]
        # ! output = [1,4,2,3]
        dummy = ListNode(next = head)
        mid = self.get_mid_list(head)
        left = mid

        left = self.reverse_list(left)
        prev,current = None, head
        while current != mid:
            prev = current
            current = current.next
        prev.next = None
        list1 = dummy.next
        dummy.next = self.mergeList(list1,left)

        return dummy.next

    def mergeList(self,list1,list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        list1.next = self.mergeList(list2,list1.next)
        return list1

    def get_mid_list(self, head):
        # * Fast and slow pointer where the slow pointer will fall in the middle whenever the fast pointer reaches the end of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head: Optional[ListNode]):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

