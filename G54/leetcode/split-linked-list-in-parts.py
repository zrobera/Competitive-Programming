# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def linkedListLength(node):
            length = 0
            curr = node
            while curr:
                length += 1
                curr = curr.next
            return length
        length = linkedListLength(head)
        ans = []
        
        quotient, rem = divmod(length,k)
        curr = head
        while curr:
            ans.append(curr)
            limit = quotient
            if rem > 0:
                limit = quotient+1
                rem -= 1
            i = 1
            while i < limit:
                curr = curr.next
                i += 1
            nxt = curr.next
            curr.next = None
            curr = nxt
        while len(ans) < k:
            ans.append(None)
        return ans
            

        