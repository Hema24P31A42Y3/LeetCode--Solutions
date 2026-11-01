class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            c = s[r]
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            seen[c] = r
            if r - l + 1 > ans:
                ans = r - l + 1
        return ans