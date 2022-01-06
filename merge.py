class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ret=[intervals[0]]
        for element in intervals[1:]: 
            if element[0]<=ret[-1][1]:
                ret[-1][1]=max(element[1], ret[-1][1] )
            else: 
                ret.append(element)
        return ret
