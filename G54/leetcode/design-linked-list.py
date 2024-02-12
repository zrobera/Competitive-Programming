class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = Node(float('inf'))

    def get(self, index: int) -> int:
        curr = self.head.next
        idx = 0
        while curr:
            if idx == index:
                return curr.val
            curr = curr.next
            idx += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        self.head.next = new

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        idx = 0
        while curr and idx < index:
            curr = curr.next
            idx += 1
        if not curr: 
            return
        new = Node(val)
        new.next = curr.next
        curr.next = new

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        idx = 0
        while curr and idx < index:
            curr = curr.next
            idx += 1
        if not curr or not curr.next: 
            return
        curr.next = curr.next.next 

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)