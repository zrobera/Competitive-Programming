class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head

        while current:
            length += 1
            current = current.next
        current =  head
        m = length-n
        count = 0
        if count == m:
            if not head.next:
                head = None
                return head
            head = head.next
            return head
        while current:
            count += 1
            if count == m:
                current.next = current.next.next
                return head
            current = current.next
