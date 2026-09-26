class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mappings = {key: value for key, value in knowledge}
        n = len(s)
        i = j = 0
        res = ""
        while j < n:
            if s[i] == "(":
                while s[j] != ")":
                    j += 1

                key = s[i + 1: j]
                res += mappings.get(key, "?")
                i = j = j + 1
            else:
                res += s[i]
                i += 1
                j += 1
        return res

