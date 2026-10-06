class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0   # Count of unmatched '('
        right = 0  # Count of unmatched ')'

        for ch in s:
            if ch == '(':
                # Store this opening parenthesis.
                # It can match a future ')'.
                left += 1
            else:
                # If an unmatched '(' exists,
                # use it to match the current ')'.
                if left:
                    left -= 1
                else:
                    # No '(' is available for this ')'.
                    # We need to insert an '(' before it.
                    right += 1

        # Remaining '(' need ')' and unmatched ')' need '('.
        # Each one requires exactly one insertion.
        return left + right