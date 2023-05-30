# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        linked_list = []
        cur = head
        while cur:
            linked_list.append(cur.val)
            cur = cur.next
        i,j = 0, len(linked_list)-1
        max_sum = 0
        while i<j:
            sums = linked_list[i] + linked_list[j]
            max_sum = max(max_sum,sums)
            i += 1
            j -= 1
        return max_sum
