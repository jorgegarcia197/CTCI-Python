from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0
        previous = ListNode(0)
        while current:
            count += 1
            current = current.next
        current = head
        if (count-n) == 0:
            head = current.next
        else:
            for i in range((count-n)):
                previous = current
                current = current.next
            previous.next = current.next
        return head



if __name__ == "__main__":
    input_value = [1, 2]
    for i in range(len(input_value)):
        input_value[i] = ListNode(input_value[i])
        if i != 0:
            input_value[i-1].next = input_value[i]
    head = input_value[0]
    solution = Solution().remove_kth_to_last_node(head, 2)
    while solution:
        print(solution.val)
        solution = solution.next
