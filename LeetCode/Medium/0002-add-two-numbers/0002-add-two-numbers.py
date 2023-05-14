# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_value = 0

        root = ListNode()
        node = root
        while l1 or l2:
            if l1:
                sum_value += l1.val
                l1 = l1.next
            
            if l2:
                sum_value += l2.val
                l2 = l2.next
            
            node.next = ListNode(val=sum_value % 10, next=None)
            sum_value = sum_value // 10

            node = node.next

        if sum_value != 0:
            node.next = ListNode(val=sum_value, next=None)

        return root.next
