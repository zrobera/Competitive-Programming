class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.stack = [homepage]
        self.fwdstack = []
        
    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.fwdstack = []
    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.stack == [self.homepage]:
                break
            self.fwdstack.append(self.stack.pop())
        return self.stack[-1] if self.stack else self.homepage
    def forward(self, steps: int) -> str:
        x = self.stack[-1]
        for i in range(steps):
            if not self.fwdstack:
                break
            x= self.fwdstack.pop()
            self.stack.append(x)
        return x



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
