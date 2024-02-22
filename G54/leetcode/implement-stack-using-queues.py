class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while self.queue1:
            for num in self.queue1:
                self.queue2.append(self.queue1.pop(0))
        return self.queue2.pop()

    def top(self) -> int:
        while self.queue1:
            for num in self.queue1:
                self.queue2.append(self.queue1.pop(0))
        return self.queue2[-1]

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()