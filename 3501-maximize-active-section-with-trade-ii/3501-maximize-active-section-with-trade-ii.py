from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        ones_start = []
        ones_end = []
        
        i = 0
        total_ones = 0
        while i < n:
            if s[i] == '1':
                st = i
                while i < n and s[i] == '1':
                    i += 1
                ones_start.append(st)
                ones_end.append(i - 1)
                total_ones += (i - st)
            else:
                i += 1
                
        M = len(ones_start)
        if M == 0:
            return [0] * len(queries)
        zero_left_start = [0] * M
        zero_right_end = [0] * M
        V = [0] * M
        
        for k in range(M):
            z_left_st = ones_end[k - 1] + 1 if k > 0 else 0
            z_right_en = ones_start[k + 1] - 1 if k < M - 1 else n - 1
            
            zero_left_start[k] = z_left_st
            zero_right_end[k] = z_right_en
            
            len_left = ones_start[k] - z_left_st
            len_right = z_right_en - ones_end[k]
            V[k] = len_left + len_right
        LOG = M.bit_length()
        st_table = [V]
        for j in range(1, LOG):
            prev = st_table[-1]
            half = 1 << (j - 1)
            curr = [0] * (M - (1 << j) + 1)
            for k_idx in range(len(curr)):
                curr[k_idx] = max(prev[k_idx], prev[k_idx + half])
            st_table.append(curr)

        def query_rmq(L: int, R: int) -> int:
            if L > R:
                return 0
            length = R - L + 1
            k_log = length.bit_length() - 1
            return max(st_table[k_log][L], st_table[k_log][R - (1 << k_log) + 1])
        ans = []
        for l, r in queries:
            idx_start = bisect_left(ones_start, l + 1)
            idx_end = bisect_right(ones_end, r - 1) - 1
            
            if idx_start > idx_end:
                ans.append(total_ones)
                continue
                
            if idx_start == idx_end:
                k = idx_start
                l0 = ones_start[k] - max(l, zero_left_start[k])
                l2 = min(r, zero_right_end[k]) - ones_end[k]
                gain = l0 + l2
                ans.append(total_ones + gain)
            else:
                k_first = idx_start
                l0_f = ones_start[k_first] - max(l, zero_left_start[k_first])
                l2_f = zero_right_end[k_first] - ones_end[k_first]
                gain_first = l0_f + l2_f
                k_last = idx_end
                l0_l = ones_start[k_last] - zero_left_start[k_last]
                l2_l = min(r, zero_right_end[k_last]) - ones_end[k_last]
                gain_last = l0_l + l2_l
                max_gain = max(gain_first, gain_last)
                if idx_start + 1 <= idx_end - 1:
                    mid_max = query_rmq(idx_start + 1, idx_end - 1)
                    if mid_max > max_gain:
                        max_gain = mid_max
                        
                ans.append(total_ones + max_gain)
                
        return ans     