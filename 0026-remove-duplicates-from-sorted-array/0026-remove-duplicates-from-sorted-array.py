class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        slow = 0

        # fast pointer anni elements ni chusthundi
        for fast in range(1, len(nums)):
            # Kottha unique number dorikithe
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        # slow + 1 eh unique count
        return slow + 1