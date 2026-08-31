
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_critical_idx: int = -1
        prev_critical_idx: int = -1
        critical_idx_cnt: int = 0
        curr_idx: int = 0
        mini_dist: int = float("inf")
        maxi_dist: int = float("-inf")
        prev_val: int = 0

        move: ListNode = head

        while move is not None:
            if curr_idx != 0 and move.next is not None:
                if ((move.val > prev_val and move.val > move.next.val) or
                    (move.val < prev_val and move.val < move.next.val)
                    ):
                    critical_idx_cnt += 1

                    if critical_idx_cnt == 1:
                        first_critical_idx = curr_idx
                    else:
                        mini_dist = min(mini_dist, curr_idx - prev_critical_idx)

                    prev_critical_idx = curr_idx

            prev_val = move.val
            curr_idx += 1
            move = move.next

        maxi_dist = max(maxi_dist, prev_critical_idx - first_critical_idx)

        if critical_idx_cnt < 2:
            return [-1, -1]
        else:
            return [mini_dist, maxi_dist]