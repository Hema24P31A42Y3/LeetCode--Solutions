class Solution:
    def longestValidParentheses(self, s):
        # Stack lo characters kadu, INDEX lu pedatham
        # -1 enduku ante, first valid string ki mundhu base kavali
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                # '(' index ni stack lo vey
                stack.append(i)
            else:
                # ')' vachindi - pair kosam okati pop chey
                stack.pop()

                # Stack khali ayithe - Idi kottha base
                # Ex: ")()(" lo first ')' tharuvatha base maripothundi
                if not stack:
                    stack.append(i)
                else:
                    # Ippudu top nunchi i varaku motham valid
                    # Length = i - stack[-1]
                    length = i - stack[-1]
                    if length > max_len:
                        max_len = length

        return max_len