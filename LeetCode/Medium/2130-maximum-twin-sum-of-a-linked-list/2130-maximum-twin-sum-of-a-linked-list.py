# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        values = list()
        node = head
        while node:
            length += 1
            values.append(node.val)
            
            node = node.next
            
        answer = 0
        for index in range(0, length // 2):
            sum_value = values[index] + values[length - index - 1]
            
            if sum_value > answer:
                answer = sum_value
                
        return answer