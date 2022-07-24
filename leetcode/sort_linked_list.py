from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self,head:Optional[ListNode])-> ListNode:
        if not head or not head.next:
            return head
        # * Get the middle of the list 
        mid = self.get_mid_list(head)
        # * Spit the list into halves, mid1 is the right half
        mid1 = mid.next
        # * Set the mid.next to None to break the list
        mid.next = None

        l = self.sortList(head)
        r = self.sortList(mid1)
        # * Sort the left and right halves
        res = self.merge_sort(l,r)

        return res
    def merge_sort(self,left,right):
        # * if not left or not right, return the other
        if not left:
            return right
        if not right:
            return left
        # * Initialize the empty list
        res = None
        # * If the left node is less than the right node, add it to the list
        if left.val <= right.val:
            res = left
            res.next = self.merge_sort(left.next,right)
        # * If the right node is less than the left node, add it to the list
        else:
            res = right
            res.next = self.merge_sort(left,right.next)
        return res
        


    def get_mid_list(self,head):
        # * Fast and slow pointer where the slow pointer will fall in the middle whenever the fast pointer reaches the end of the list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


