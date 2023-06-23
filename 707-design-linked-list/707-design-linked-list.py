class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        if index < 0 or index >= self.size:
            return -1
        current=self.head
        while index>0:
            current=current.next
            index-=1
        return current.val

    def addAtHead(self, val: int) -> None:
        node=ListNode(val,self.head)
        self.head=node
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        current=self.head
        node=ListNode(val,None)
        if current is None:
            self.head=node
        else:
            while current.next:
                current=current.next
            current.next=node
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            prev=self.head
            while index>1:
                prev=prev.next
                index-=1
            cur=ListNode(val,None)
            succ=prev.next
            prev.next=cur
            cur.next=succ
            self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)