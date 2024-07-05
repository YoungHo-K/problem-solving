# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None:
            return [-1, -1]
        
        numbers = []
        while head:
            numbers.append(head.val)
            head = head.next
        
        critical_points = []
        for index in range(1, len(numbers) - 1):
            current_value = numbers[index]
            
            if (numbers[index - 1] < current_value) and (current_value > numbers[index + 1]):
                critical_points.append(index)

            if (current_value < numbers[index - 1]) and (current_value < numbers[index + 1]):
                critical_points.append(index)
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        critical_points.sort()
        
        max_dist = critical_points[-1] - critical_points[0]
        min_dist = float("inf")
        for index in range(1, len(critical_points)):
            diff = critical_points[index] - critical_points[index - 1]
            
            if diff < min_dist:
                min_dist = diff
        
        return [min_dist, max_dist]
