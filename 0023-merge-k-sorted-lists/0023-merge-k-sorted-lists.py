# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        heap = []
        for i in range(len(lists)):
            curr = lists[i]
            if curr:
                heapq.heappush(heap, (curr.val, i , curr))
        dummy = ListNode()
        curr = dummy
        while heap:
            _, idx, li = heapq.heappop(heap)
            curr.next = li
            if li.next:
                heapq.heappush(heap, (li.next.val, idx, li.next))
            li.next = None
            curr = curr.next
        return dummy.next