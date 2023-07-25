# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        root = ListNode()
        node = root
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    node.next = ListNode(val=list1.val, next=None)
                    list1 = list1.next                
                else:
                    node.next = ListNode(val=list2.val, next=None)
                    list2 = list2.next

            elif list1:
                node.next = ListNode(val=list1.val, next=None)
                list1 = list1.next                
        
            elif list2:
                node.next = ListNode(val=list2.val, next=None)
                list2 = list2.next
                
            node = node.next

        return root.next
        