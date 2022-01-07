import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0
        events.sort(key=lambda x:x[0])
        curr_day=events[0][0]
        counter=0
        i=0
        start=[]
        while i<len(events):
            while i<len(events) and events[i][0]==curr_day: 
                heappush(start, events[i][1])
                i+=1
            
            heappop(start)
            counter+=1
            curr_day+=1
            
            while start and start[0]<curr_day: 
                heappop(start)
            if i<len(events) and not start: 
                curr_day=events[i][0]
                
        while start: 
            if heappop(start)>=curr_day: 
                curr_day+=1
                counter+=1
                
        return counter
