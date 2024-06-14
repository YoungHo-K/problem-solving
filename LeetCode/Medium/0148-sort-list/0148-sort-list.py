# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None):
            return head
        
        
        heap = []
        node = head
        while node:
            heapq.heappush(heap, node.val)
            node = node.next
            
        root = ListNode()
        node = root
        while heap:
            value = heapq.heappop(heap)
            
            node.next = ListNode(value)
            node = node.next
            
        return root.next
        