class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # 1. Pivot kanukko - Right nunchi first down ayye place
        # Ex: [1,2,3] lo 1 < 2 kabatti pivot = 1 (index 1)
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # Pivot dorakakapothe - Idi eh last permutation
        # Ex: [3,2,1] -> Reverse cheste first permutation [1,2,3] vasthundi
        if pivot == -1:
            nums.reverse()
            return

        # 2. Pivot kanna konchem pedda number ni Right nunchi kanukko
        for j in range(n - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                # Swap chey
                temp = nums[pivot]
                nums[pivot] = nums[j]
                nums[j] = temp
                break

        # 3. Pivot tharuvatha unna dani motham reverse chey
        # Endukante adi descending lo untundi, dani ascending cheyali
        left = pivot + 1
        right = n - 1
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1