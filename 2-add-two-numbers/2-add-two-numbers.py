# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        sum1 = 0
        sum2 = 0
        i = 1
        while current1 and current2:
            sum1 += current1.val * i
            sum2 += current2.val * i
            i *= 10
            current1 = current1.next
            current2 = current2.next

        while current1:
            sum1 += current1.val * i
            i *= 10
            current1 = current1.next

        while current2:
            sum2 += current2.val * i
            i *= 10
            current2 = current2.next

        sum3 = sum1 + sum2
        head = ListNode(sum3 % 10)
        current = head
        sum3 //= 10
        while sum3 > 0:
            current.next = ListNode(sum3 % 10)
            sum3 //= 10
            current = current.next

        return head

