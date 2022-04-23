class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sum_list(list1, list2):
    current1 = list1
    current2 = list2
    remainder = 0
    head = node = None
    while current1 or current2:
        if not current1:
            sum_value = current2.val + remainder
            current2 = current2.next
            remainder = sum_value // 10
        elif not current2:
            sum_value = current1.val + remainder
            current1 = current1.next
            remainder = sum_value // 10
        else:
            sum_value = current1.val + current2.val + remainder
            remainder = sum_value // 10
        current1 = current1.next
        current2 = current2.next
        add = sum_value % 10

        # if node is None add head, else the next node
        if node is None:
            head = node = ListNode(val=add)
        else:
            node.next = ListNode(add)
            node = node.next
    return head


if __name__ == '__main__':
    list1 = ListNode(7, ListNode(1, ListNode(6)))
    list2 = ListNode(5, ListNode(9, ListNode(2)))
    output = sum_list(list1, list2)
    while output:
        print(output.val)
        output = output.next
