class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        max1, max2, max3 = 0, 0, 0
        min1, min2, min3 = 10**9 + 1, 10**9 + 1, 10**9 + 1

        # With 3 elements, we can make all values equal
        if len(nums) == 3:
            return 0

        for n in nums:
            # Track the three largest elements
            if max1 < n:
                max1, max2, max3 = n, max1, max2
            elif max2 < n:
                max2, max3 = n, max2
            elif max3 < n:
                max3 = n

            # Track the three smallest elements
            if min1 > n:
                min1, min2, min3 = n, min1, min2
            elif min2 > n:
                min2, min3 = n, min2
            elif min3 > n:
                min3 = n
        return min(
            max3 - min1,  # Change the two largest
            max2 - min2,  # Change the smallest and largest
            max1 - min3   # Change the two smallest
        )