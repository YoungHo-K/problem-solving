# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        beginning_node = None
        node = head
        while node:
            length += 1
            if length == k:
                beginning_node = node
                
            node = node.next

        stopped_index = 0
        swapping_node = head
        while stopped_index < length - k:
            stopped_index += 1
            
            swapping_node = swapping_node.next
            
        temp = beginning_node.val
        beginning_node.val = swapping_node.val
        swapping_node.val = temp
        
        return head