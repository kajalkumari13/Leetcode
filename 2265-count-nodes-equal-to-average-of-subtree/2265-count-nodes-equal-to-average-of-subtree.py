class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left_sum, left_count = left >> 32, left & 0xFFFFFFFF
            right_sum, right_count = right >> 32, right & 0xFFFFFFFF

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if node.val == (total_sum // total_count):
                ans += 1

            return (total_sum << 32) | total_count

        dfs(root)
        return ans