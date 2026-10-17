class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def f(n):
            s,t=0,n
            while n:
                s+=n%10
                n//=10
            return (s,t)
        sl=sorted(nums,key=f)
        h={nums[i]:i for i in range(len(nums))}
        c=0
        for i in range(len(nums)):
            if sl[i]!=nums[i]:
                x,y=h[sl[i]],h[nums[i]]
                h[nums[i]],h[sl[i]]=x,y
                nums[y],nums[x]=sl[i],nums[i]
                c+=1
        return c
        