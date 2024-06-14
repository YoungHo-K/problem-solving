# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        node = root
        sum_value = 0
        
        while l1 or l2:
            if l1:
                sum_value += l1.val
                l1 = l1.next
            
            if l2:
                sum_value += l2.val
                l2 = l2.next

            node.next = ListNode(val=sum_value % 10)                
            node = node.next
            
            sum_value //= 10
            
        if sum_value != 0:
            node.next = ListNode(val=sum_value)

        return root.next
