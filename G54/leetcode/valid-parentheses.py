class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicts  = {"(": ")", "[":"]", "{": "}"}
        for char in s:
            if char in dicts:
                stack.append(char)
            else:
                if not stack or (stack and dicts[stack.pop()] != char):
                    return False
        return len(stack) == 0
        