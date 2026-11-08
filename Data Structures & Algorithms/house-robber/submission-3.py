class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2,prev=0,0
        for num in nums:
            temp=max(prev2+num,prev)
            prev2=prev
            prev= temp
        return prev
         

        
        