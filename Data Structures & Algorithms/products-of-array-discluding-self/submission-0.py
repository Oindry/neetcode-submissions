class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
       
        for index,val in enumerate(nums):
            dupli= nums.copy()
            dupli.pop(index)
            multi=1
            for i,v in enumerate(dupli):
                multi= v*multi 
            output.append(multi)
        return output   
        

        