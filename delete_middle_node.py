# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        temp = head
        if not head:
            return None
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        if fast == head:
            head = None
            return head
        temp.next = temp.next.next
        return head
