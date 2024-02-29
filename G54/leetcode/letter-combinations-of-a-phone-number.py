class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        
        def backtrack(combination, remaining):
            if not remaining:
                ans.append(combination)
                return
            
            for letter in phone[remaining[0]]:
                initial = combination
                combination += letter
                backtrack(combination, remaining[1:])
                combination = initial
        
        backtrack("", digits)
        return ans