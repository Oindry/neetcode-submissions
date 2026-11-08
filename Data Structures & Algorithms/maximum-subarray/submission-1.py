class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum= -1e9
        curSum=0
        for n in nums:
            curSum= max(curSum,0)
            curSum+= n
            maxSum=max(maxSum,curSum)

        return maxSum
            
        