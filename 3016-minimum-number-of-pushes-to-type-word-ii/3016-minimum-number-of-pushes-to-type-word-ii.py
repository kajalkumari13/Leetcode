from collections import Counter
class Solution:
    def minimumPushes(self, word):
        d=dict(Counter(word))
        items=[]
        for i in d:
            items.append((d[i],i))
        items.sort(reverse=True)
        c=0
        for k in range(len(items)):
            i,j=items[k]
            if k<=7:
                c+=i
            elif k>7 and k<=15:
                c+=(2*i)
            elif k>15 and k<=23:
                c+=(3*i)
            elif k>23 and k<26:
                c+=(4*i)
        return c