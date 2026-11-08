class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dfs(i,remain):
            if  remain==0:
                return 0
            if (i,remain) in memo:
                return memo[(i,remain)]
            if i >= len(coins) or remain<0:
                return float('inf')
            #use cae
            use= 1+ dfs(i,remain-coins[i])
            #skip
            skip= dfs(i+1,remain)
            
            result = min(use, skip)
            memo[(i, remain)] = result
            return result
    
        result = dfs(0, amount)
        return -1 if result == float('inf') else result
