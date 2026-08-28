from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, t: str) -> str:
        C = Counter(s)
        mid = "".join(c for c, v in C.items() if v % 2)
        if len(mid) > 1: return ""
        
        R, m, k = Counter({c: v // 2 for c, v in C.items()}), len(s) // 2, 0
        while k < m and R[t[k]]: R[t[k]] -= 1; k += 1
            
        if k == m and (ans := t[:m] + mid + t[:m][::-1]) > t: return ans
        
        for i in range(k, -1, -1):
            if i < k: R[t[i]] += 1
            if i < m and (nxt := next((c for c in sorted(R) if R[c] and c > t[i]), "")):
                R[nxt] -= 1
                L = t[:i] + nxt + "".join(sorted(R.elements()))
                return L + mid + L[::-1]
                
        return ""
        