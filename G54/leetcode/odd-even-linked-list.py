# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        curr1 = head
        curr2 = head.next 
        head2 = curr2 
        
        while curr2 and curr2.next: 
            curr1.next = curr1.next.next
            curr2.next = curr2.next.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        curr1.next = head2
        
        return head