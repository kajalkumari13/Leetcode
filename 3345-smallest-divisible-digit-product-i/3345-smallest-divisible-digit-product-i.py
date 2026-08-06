class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while n < 101:
            digits = n
            product = 1

            while digits > 0:
                product *= digits % 10
                digits //= 10

            if product % t == 0:
                return n

            n += 1

        return 0