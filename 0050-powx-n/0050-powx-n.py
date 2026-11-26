class Solution:
    def myPow(self, x, n):
        # base case
        if n == 0:
            return 1
        
        # n negative aithe
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # n even aithe
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        # n odd aithe
        else:
            half = self.myPow(x, n // 2)
            return x * half * half