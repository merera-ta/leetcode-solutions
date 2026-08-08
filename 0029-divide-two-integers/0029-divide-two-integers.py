class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Special overflow case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Convert to positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            value = divisor
            multiple = 1

            # Keep doubling the divisor
            while (value << 1) <= dividend:
                value <<= 1
                multiple <<= 1

            dividend -= value
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        return quotient