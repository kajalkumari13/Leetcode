MOD = 10 ** 9 + 7
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        @functools.cache
        def dp(idx: int, gcd1: int, gcd2: int) -> int:
            if idx == len(nums):
                return int(gcd1 == gcd2 and gcd1 != 0)

            return (
                dp(idx + 1, gcd1, gcd2) + 
                dp(idx + 1, gcd(gcd1, nums[idx]), gcd2) + 
                dp(idx + 1, gcd1, gcd(gcd2, nums[idx]))
            ) % MOD

        return dp(0, 0, 0)       
        