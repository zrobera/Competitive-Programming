class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_brackets = n
        closed_brackets = n
        ans = []
        current = ""
        def backtrack(opens,closes,curr):
            nonlocal ans
            if closes == 0:
                ans.append(curr)
                return ans
            if closes == opens and opens > 0:
                backtrack(opens-1,closes, curr + "(")
            elif closes > opens and opens > 0:
                backtrack(opens-1,closes, curr + "(")
                backtrack(opens,closes-1, curr + ")")
            elif closes > opens and opens == 0:
                backtrack(opens,closes-1, curr + ")")

        backtrack(open_brackets,closed_brackets,current)
        return ans
        