# Solution from here: https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code/148769
# The left-shift operation results in a better running time


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) == (divisor < 0)
        dividend, divisor, quotient = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            bitwise_left_shift_operations = 0
            while dividend >= divisor << (bitwise_left_shift_operations + 1):
                bitwise_left_shift_operations += 1
            quotient += 1 << bitwise_left_shift_operations
            dividend -= divisor << bitwise_left_shift_operations
        return min(quotient if sign else -quotient, 2147483647)


solution = Solution()
print(solution.divide(10003, 3))
