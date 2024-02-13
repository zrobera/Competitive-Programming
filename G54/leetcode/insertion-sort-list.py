# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        right = head
        while right:
            left = head
            while left != right:
                if right.val < left.val:
                    right.val, left.val = left.val, right.val
                left = left.next
            right = right.next
        return head
