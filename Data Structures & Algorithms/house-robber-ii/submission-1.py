class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2,prev=0,0
        firstcase=0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            temp= max(nums[i]+prev2,prev)
            prev2=prev
            prev=temp

        firstcase= prev
        prev2,prev=0,0
        secondcase=0
        for i in range(1,len(nums)):
            temp= max(nums[i]+prev2,prev)
            prev2=prev
            prev=temp
        secondcase=prev

        return max(firstcase,secondcase)

        
        