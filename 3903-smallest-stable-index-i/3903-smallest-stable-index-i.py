class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        for i in range(n):
            maxi = max(nums[:i + 1])
            mini = min(nums[i:])

            if maxi - mini <= k:
                return i

        return -1