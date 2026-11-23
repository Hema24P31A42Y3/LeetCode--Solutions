class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Prathi number ni correct place lo pettu
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # swap chey
                correct_pos = nums[i] - 1
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        
        # Step 2: First wrong place kanukko
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Anni correct ga unte, next number ye answer
        return n + 1