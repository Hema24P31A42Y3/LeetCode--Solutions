class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, current):
            if index == len(digits):
                res.append(current)
                return
            
            letters = mapping[digits[index]]
            for ch in letters:
                backtrack(index + 1, current + ch)
        
        backtrack(0, "")
        return res