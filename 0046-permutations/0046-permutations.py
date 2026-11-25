class Solution:
    def permute(self, nums):
        res = []
        path = []
        used = [False] * len(nums)
        
        def backtrack():
            # path full ayithe oka permutation dorikindi
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                # ee number already vadam ledu ani check
                if used[i]:
                    continue
                # 1. Pettu
                used[i] = True
                path.append(nums[i])
                # 2. Vellu
                backtrack()
                # 3. Theesey (Backtrack)
                path.pop()
                used[i] = False
        
        backtrack()
        return res