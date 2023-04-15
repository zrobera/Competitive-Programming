class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {"{": "}", "(": ")", "[": "]"}
        opening_bracket = ["(", "{", "["]
        closing_bracket = [")", "}", "]"]
        stack1 = list(s)
        stack2 = []
        while len(stack1) > 0:
            current = stack1.pop()
            if current in closing_bracket:
                stack2.append(current)
            elif current in opening_bracket:
                if not stack2:
                    return False
                current2 = stack2.pop()
                if current2 != p_dict[current]:
                    return False
        if not stack1 and not stack2:
            return True
        else:
            return False
