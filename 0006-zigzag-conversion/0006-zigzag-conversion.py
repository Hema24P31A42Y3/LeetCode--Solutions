class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        res = [""] * numRows
        i = 0
        step = 1
        
        for char in s:
            res[i] += char
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step
            
        return "".join(res)