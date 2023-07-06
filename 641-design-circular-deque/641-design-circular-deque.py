class MyCircularDeque:
    def __init__(self, k: int):
        self.size = 0
        self.front = 0
        self.rear = 0
        self.k = k
        self.deque = [0] * k
    
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.deque[self.front] = value
        else:
            self.front = (self.front - 1) % self.k
            self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.deque[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.k
            self.deque[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque[self.front] = -1
        self.front = (self.front + 1) % self.k
        self.size -= 1
        if self.isEmpty():
            self.rear = self.front
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque[self.rear] = -1
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear
        return True
    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
