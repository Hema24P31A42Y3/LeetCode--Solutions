class Solution:
    def searchRange(self, nums, target):
        # First position kanukko
        first = self.find_bound(nums, target, True)
        # First eh dorakakapothe target ye ledu
        if first == -1:
            return [-1, -1]
        # Last position kanukko
        last = self.find_bound(nums, target, False)
        return [first, last]

    def find_bound(self, nums, target, is_first):
        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                # First kavali ante - inka left ki vellu
                # Last kavali ante - inka right ki vellu
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans