class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                # Ippati closest kanna ee total target ki daggralo unte update chey
                if abs(total - target) < abs(closest - target):
                    closest = total
                
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return total
        return closest