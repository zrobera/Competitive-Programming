# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow  = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        curr = head
        slow = prev
        while slow:
            if slow.val != curr.val:
                return False
            slow = slow.next
            curr = curr.next
        return True
        