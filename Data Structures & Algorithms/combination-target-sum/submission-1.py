class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]: 
        res=[]
        def dfs(i,remain,cur):
            if(remain==0):
                res.append(cur.copy())
                return 
            if(remain<0 or i >= len(nums)):
                return
            #take
            cur.append(nums[i])
            dfs(i,remain-nums[i],cur)
            cur.pop()
            dfs(i+1,remain,cur)

        dfs(0,target,[])

        return res
