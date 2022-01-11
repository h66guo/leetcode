from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue= deque()
        counter=0
        fresh=0
        time=-1
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if grid[i][j]==2: 
                    queue.append((i,j))
                    
                elif grid[i][j]==1: 
                    fresh+=1
                    
        queue.append((-1,-1))
                    
        while queue: 
            row, col= queue.popleft()
            if row==-1: 
                time+=1
                if queue: 
                    queue.append((-1,-1 ))
            neighbor=[[row+1, col], [row-1, col], [row, col+1], [row,col-1]]
            
            for element in neighbor: 
                if element[0]>=0 and element[0]<len(grid) and element[1]>=0 and element[1]<len(grid[0]):
                    if grid[element[0]][element[1]]==1: 
                        grid[element[0]][element[1]]=2
                        fresh-=1
                        
                        queue.append((element[0], element[1]))
        if fresh==0: 
            return time
        else: 
            return -1
            
                     
