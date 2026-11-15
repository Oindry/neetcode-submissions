class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #BruteForce:
        n = len(nums)
        res = [0] * n
        prod=1
        zero_cnt=0
        for i in range(n):
            if nums[i]==0:
                zero_cnt+=1
            else:
                prod= prod*nums[i]
        if zero_cnt>1 :
            return res
           
        for i in range(n):
            if nums[i]==0:
                res[i]=prod
            else:
                if zero_cnt!=0:
                    res[i]=0
                else:
                    res[i]=int(prod/nums[i])

        return res