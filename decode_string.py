class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                substring = ''
                while stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()
                num_str = ''
                while stack and stack[-1].isdigit():
                    num_str = stack.pop() + num_str
                num = int(num_str)
                substring *= num
                stack.append(substring)
            else:
                stack.append(char)
        return ''.join(stack)

        
