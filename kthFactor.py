import heapq
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ret=[]
        for i in range(1, int(n**0.5)+1):
            if n%i==0:
                ret.append(i)
                if n//i not in ret:
                    ret.append(n//i)    
                
                
        res=heapq.heapify(ret)
        if k>len(ret):
            return -1
        print(ret)
        res= heapq.nsmallest(k, ret)
        return res[-1]
