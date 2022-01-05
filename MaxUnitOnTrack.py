class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = [(-1*numUnit, numBox) for [numBox, numUnit] in boxTypes]
        heapq.heapify(heap)
        
        res = 0
        
        while heap:
            numUnit, numBox = heapq.heappop(heap)
            numUnit *= -1
            if numBox <= truckSize:
                res += numUnit * numBox
                truckSize -= numBox
                if truckSize == 0:
                    break
            else:
                res += truckSize * numUnit
                break
        
        return res
