class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count, last_end = 0, -1

        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k and left > last_end:
                    count += 1
                    last_end = right
                    break
                left -= 1
                right += 1

        return count