import heapq 
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict=Counter(arr)
        
        valdict=sorted(dict.values())
        count=len(dict)
        for value in valdict: 
            if value<k:
                k-=value
                count-=1
            elif value==k: 
                count-=1
                return count
            else: 
                return count
        # return len(sort_orders)

        
