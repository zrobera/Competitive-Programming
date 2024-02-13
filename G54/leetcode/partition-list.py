# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        dummy1, dummy2 = ListNode(), ListNode()
        curr1 = dummy1
        curr2 = dummy2
        while curr:
            if curr.val < x:
                curr1.next = curr
                curr1 = curr1.next
            else:
                curr2.next = curr
                curr2 = curr2.next
            curr = curr.next
        curr1.next = None
        curr2.next = None
        curr1.next = dummy2.next
        return dummy1.next
        
            
            