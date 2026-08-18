class Solution:
    def largestInteger(self, a: List[int], k: int) -> int:
        if len(a)==k: return max(a)
        z = Counter(chain(*(a[i:i+k] for i in range(len(a)-k+1))))
        return max((v for v in z if z[v]==1),default=-1)