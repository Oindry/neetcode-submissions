class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxVal = 0
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        
        def dfs(r, c, val) -> int:
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            visit.add((r, c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc, val)
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    val = dfs(r, c, 1)
                    maxVal = max(maxVal, val)
                
        return maxVal