class Solution:
    def divide(self, dividend, divisor):
        # Overflow case - LeetCode special case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Sign kanukko - okati negative aithe answer negative
        negative = (dividend < 0) != (divisor < 0)

        # Anni positive chesuko
        a = abs(dividend)
        b = abs(divisor)
        result = 0

        # a lo b inka undannantha varaku
        while a >= b:
            temp = b
            multiple = 1

            # temp ni double chesthu vellu, a ni datakunda
            while a >= temp + temp:
                temp = temp + temp
                multiple = multiple + multiple

            a = a - temp
            result = result + multiple

        if negative:
            result = -result

        return result