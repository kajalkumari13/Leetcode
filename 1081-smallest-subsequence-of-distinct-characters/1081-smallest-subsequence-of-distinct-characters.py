class Solution:
    def smallestSubsequence(self, s: str) -> str:
        size: int = len(s)
        stack: list[chr] = []
        suffix: list[int] = [0] * 26
        visited: list[bool] = [False] * 26 

        for i in range(0, size):
            suffix[ord(s[i]) - ord('a')] = i

        for i in range(0, size):
            if visited[ord(s[i]) - ord('a')] is False:
                while (len(stack) != 0 and 
                        stack[-1] > s[i] and 
                        suffix[ord(stack[-1]) - ord('a')] > i
                    ):
                    popped: chr = stack.pop()
                    visited[ord(popped) - ord('a')] = False

                stack.append(s[i])
                visited[ord(s[i]) - ord('a')] = True

        return "".join(stack)