class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        n = len(word)
        row = 1
        quotient = n // 8
        remainder = n % 8

        while quotient > 0:
            ans += 8 * row

            quotient -= 1
            row += 1

        ans += remainder * row

        return ans