class Solution:
    def maxDiffSubArrays(self, arr):
        n = len(arr)
        if n < 2:
            return 0

        left_max = [0] * n
        left_min = [0] * n
        right_max = [0] * n
        right_min = [0] * n

        cur_max = cur_min = arr[0]
        left_max[0] = left_min[0] = arr[0]
        best_max = best_min = arr[0]

        for i in range(1, n):
            cur_max = max(arr[i], cur_max + arr[i])
            best_max = max(best_max, cur_max)
            left_max[i] = best_max

            cur_min = min(arr[i], cur_min + arr[i])
            best_min = min(best_min, cur_min)
            left_min[i] = best_min

        cur_max = cur_min = arr[n - 1]
        right_max[n - 1] = right_min[n - 1] = arr[n - 1]
        best_max = best_min = arr[n - 1]

        for i in range(n - 2, -1, -1):
            cur_max = max(arr[i], cur_max + arr[i])
            best_max = max(best_max, cur_max)
            right_max[i] = best_max

            cur_min = min(arr[i], cur_min + arr[i])
            best_min = min(best_min, cur_min)
            right_min[i] = best_min

        ans = 0
        for i in range(n - 1):
            ans = max(ans, abs(left_max[i] - right_min[i + 1]))
            ans = max(ans, abs(right_max[i + 1] - left_min[i]))
from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # freq[x] stores how many times x appears in nums
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        # multiples[x] stores how many numbers in nums are multiples of x
        multiples = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                multiples[i] += freq[j]
                
        # exact_gcd[x] stores the exact number of pairs with GCD == x
        exact_gcd = [0] * (max_val + 1)
        
        # Traverse backwards to use Inclusion-Exclusion
        for i in range(max_val, 0, -1):
            count = multiples[i]
            # Total possible pairs where both elements are multiples of i
            pairs = count * (count - 1) // 2 
            
            # Subtract pairs where the GCD is a strict multiple of i
            for j in range(i * 2, max_val + 1, i):
                pairs -= exact_gcd[j]
                
            exact_gcd[i] = pairs
            
        # Prefix sums to answer index-based queries
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + exact_gcd[i]
            
        # Answer each query using binary search
        ans = []
        for q in queries:
            # Find the smallest index where prefix sum is greater than the query index
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans
        return ans