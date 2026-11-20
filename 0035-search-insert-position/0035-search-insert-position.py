class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Dorikindi
            if nums[mid] == target:
                return mid
            # Target mid kanna chinna - left side ki vellu
            elif nums[mid] > target:
                right = mid - 1
            # Target mid kanna pedda - right side ki vellu
            else:
                left = mid + 1

        # Dorakaledu - Ikkada insert cheyali, ade left
        return left