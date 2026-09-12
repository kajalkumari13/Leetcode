from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        
        # intervals[i] = [start, end, weight]
        # DP + Binary Search

        n = len(intervals)

        # Store: [end, start, weight, original_index]
        # We keep original_index because sorting will change the order
        arr = [(intervals[i][1], intervals[i][0], intervals[i][2], i) for i in range(n)]

        # sort by end-time for overlapping interval problems
        arr.sort(key = lambda x: x[0])

        # DP Table: dp[i][j] = maximum score using the first i intervals
        # while choosing at most j intervals
        # j can be 0, 1, 2, 3, or 4
        dp = [[0] * 5 for _ in range(n + 1)]

        # Store the original indices that produced each DP answer
        indices = [[ [] for _ in range(5)] for _ in range(n + 1)]

        for i in range(n):

            # Current interval
            end, start, weight, idx = arr[i]

            # Find how many previous intervals have: previous_end < current_start
            # These are the intervals that can safely be chosen
            # together with the current interval
            k = bisect_left(arr, (start,), hi = i)

            for j in range(1, 5):

                # OPTION 1: Skip the current interval
                s1 = dp[i][j]

                # OPTION 2: Take the current interval
                # We can only use compatible intervals before k
                # Since current interval uses one slot,
                # we look at j - 1 intervals there
                s2 = dp[k][j - 1] + weight

                # Indices for the two possible choices
                c1 = indices[i][j]              # Skip
                c2 = indices[k][j - 1] + [idx]  # Take

                # Keep indices sorted so that we can compare them lexicographically
                c2.sort()

                # If skipping gives a better score, keep the old answer
                # OR
                # If scores are equal, choose the smaller index list
                if s1 > s2 or (s1 == s2 and c1 < c2):

                    dp[i + 1][j] = s1
                    indices[i + 1][j] = c1.copy()

                else:

                    dp[i + 1][j] = s2
                    indices[i + 1][j] = c2

        # At most 4 intervals can be selected
        # indices[n][4] contains best answer
        return indices[n][4]
