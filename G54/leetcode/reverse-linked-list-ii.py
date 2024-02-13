# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or right == left:
            return head
        curr = head
        prev = None
        initial = None
        moves = left
        while moves > 0:
            initial = prev
            curr,prev = curr.next, curr
            moves -= 1
        middle = prev
        middle.next = None
        moves = right-left
        while curr and moves > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            moves -= 1
        if initial:
            initial.next = prev
            middle.next = curr
            return head
        else:
            middle.next = curr
            return prev

        
        