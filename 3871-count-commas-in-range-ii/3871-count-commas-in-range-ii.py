class Solution:
    def countCommas(self, n: int) -> int:
        commas_count = 0
        base_number = 999
        threshold = 999

        if n <= 999:
            return 0

        while threshold < n:
            commas_count += n - threshold
            threshold = threshold * 1000 + base_number

        return commas_count