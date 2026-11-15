class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(curr, open_count, close_count):
            # Length 2*n aythe oka valid combination dorikindi
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # Open inka migilithe '(' add chey
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Close, Open kanna thakkuva unte ne ')' add chey
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res