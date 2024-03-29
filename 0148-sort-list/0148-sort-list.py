# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur= cur.next
        nodes.sort(key=lambda x: x.val)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[len(nodes)-1].next = None
        return nodes[0]

        