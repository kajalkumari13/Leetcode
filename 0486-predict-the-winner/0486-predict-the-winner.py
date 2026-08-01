class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(arr,i,j):
            if i == j:
                return arr[i]
            left = arr[i] - winner(arr,i+1,j)
            right = arr[j] - winner(arr,i,j-1)
            return max(left,right)
        return winner(nums,0,len(nums)-1) >= 0