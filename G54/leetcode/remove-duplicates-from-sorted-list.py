# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            nxt = curr.next
            while nxt and nxt.val == curr.val:
                curr.next = nxt.next
                nxt = nxt.next
            curr = curr.next
        return head

        