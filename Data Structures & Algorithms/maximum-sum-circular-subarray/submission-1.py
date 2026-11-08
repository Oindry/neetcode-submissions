class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        golMax,golMin= nums[0],nums[0]
        curMax,curMin=-1e9,1e9
        total=0
        for n in nums:
            curMax= max(curMax+n,n)
            curMin= min(curMin+n,n)
            total+=n
            golMax=max(curMax,golMax)
            golMin=min(curMin,golMin)

        return max(golMax,total-golMin) if golMax>0 else golMax

        