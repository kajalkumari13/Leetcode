class Solution:
    def checkDivisibility(self, n: int) -> bool:
        result = [int(digit) for digit in str(n)]

        sum_n = 0
        prod_n = 1

        for i in range(len(result)):
            sum_n += result[i]
            prod_n *= result[i]

        if (sum_n + prod_n) == 0:
            return False

        if n % (sum_n + prod_n) == 0:
            return True
        else:
            return False