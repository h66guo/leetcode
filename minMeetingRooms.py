class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        heap = []
        
        import heapq
        for start, end in intervals:
            if len(heap) == 0 or start < heap[0]:
                heapq.heappush(heap, end)
            else:
                heapq.heappushpop(heap, end)
        
        return len(heap)
