class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix in one output
        n = len(nums)
        res=[0]*n
        multi=1
        for i in range(n):
            if i==0:
                res[i]=1
            else:
                res[i]= multi
            multi=multi*nums[i]
        multi=1
        for i in range(len(nums) - 1, -1, -1):
            if i==len(nums) - 1:
                res[i]=res[i]
            else:
                res[i]= multi*res[i]
            multi=multi*nums[i]

        return res