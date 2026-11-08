class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m=[]
        output=[1]*(len(nums))
        prefix=1
        for index,val in enumerate(nums):
                output[index]=prefix
                prefix= output[index]*val      
        postfix=1
        for i in range(len(nums) - 1, -1, -1):
            
            output[i]*=postfix
            postfix= nums[i]*postfix
            
        return output
        

        