from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            nums[i] *= nums[i]

        nums.sort()

        res = 0
        left, right = 0, n - 1

        while left <= right:
            if left == right:
                res += nums[left]
                break

            res += nums[right] - nums[left]
            left += 1
            right -= 1

        return res