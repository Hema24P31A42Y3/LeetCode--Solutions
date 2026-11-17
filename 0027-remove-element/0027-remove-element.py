class Solution:
    def removeElement(self, nums, val):
        slow = 0

        # fast pointer anni elements ni chusthundi
        for fast in range(len(nums)):
            # val kakunda unna dani ne mundhuku theesukovali
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        # slow eh migilina count
        return slow