class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            # Closing bracket aythe
            if ch in mapping:
                # Stack empty aythe, leda top match kakapothe False
                if not stack or stack.pop() != mapping[ch]:
                    return False
            else:
                # Opening bracket aythe stack lo push chey
                stack.append(ch)

        # Last lo stack empty aythe ne valid
        return len(stack) == 0