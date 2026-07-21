class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        return s.count('1')+max(map(sum,pairwise(map(len,findall(r'0+',s)))),default=0)