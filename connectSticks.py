import heapq   
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ret=0
        heapq.heapify(sticks)
        while len(sticks)>1:
            
            
           
            temp=heapq.heappop(sticks)+heapq.heappop(sticks)
            heapq.heappush(sticks, temp)
            ret+=temp
        
        return ret
