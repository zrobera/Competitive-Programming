class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for p in path:
            if p == ".." and stack:
                stack.pop()
            elif p == "" or p == "." or (p == ".." and not stack):
                continue
            else:
                stack.append(p)
        return "/"+"/".join(stack)
        
        