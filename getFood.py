from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        q=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="*":
                    q.append((i,j,0))
                    
        while q: 
            i, j, step=q.popleft()
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]!="X":
                if grid[i][j]=="#":
                    return step
                grid[i][j]="X"
                q.append((i+1, j, step+1))
                q.append((i-1, j, step+1))
                q.append((i, j+1, step+1))
                q.append((i, j-1, step+1))
                
        return -1
