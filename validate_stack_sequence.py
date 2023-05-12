class Solution:
    def validateStackSequences(self, pushed:List[int], popped: List[int]) -> bool:
        i = j = 0
        stack = []
        while True:
            while stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
            if i >= len(pushed):
                break
            stack.append(pushed[i])
            i += 1
        if stack:
            return False
        return True
        
