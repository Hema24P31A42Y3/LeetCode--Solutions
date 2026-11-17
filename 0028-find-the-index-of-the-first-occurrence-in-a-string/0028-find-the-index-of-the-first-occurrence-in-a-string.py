class Solution:
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)

        # needle length varaku slice chesi chusthu vellu
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        # Ekkada dorakakapothe -1
        return -1