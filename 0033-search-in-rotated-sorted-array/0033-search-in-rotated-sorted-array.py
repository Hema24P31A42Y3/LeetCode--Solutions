class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Dorikindi
            if nums[mid] == target:
                return mid

            # LEFT side sorted ga unda? [4,5,6] lanti
            if nums[left] <= nums[mid]:
                # Target ee left sorted part lo unda?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # RIGHT side sorted ga unda? [0,1,2] lanti
            else:
                # Target ee right sorted part lo unda?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1