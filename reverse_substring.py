class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                sub = stack.pop()[::-1]
                if stack:
                    stack[-1] += sub
                else:
                    stack.append(sub)
            else:
                if stack:
                    stack[-1] += c
                else:
                    stack.append(c)
        return stack[0]
