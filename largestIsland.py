class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        big=0
        N=len(grid)
        def dfs(r,c,seen):
            
            for row, col in ((r-1,c),(r,c-1), (r+1,c), (r,c+1)):
                if (row, col) not in seen and 0<=row<N and 0<=col<N and grid[row][col]:
                    seen.add((row, col))
                    dfs(row, col, seen)
            
        
        has_zero=False
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val ==0:
                    grid[r][c]=1
                    has_zero=True
                    seen={(r,c)}
                    dfs(r,c,seen)
                    # print(seen)
                    if len(seen)>big:
                        big=len(seen)
                        
                    grid[r][c]=0
                    
        return big if has_zero else N*N
                    
