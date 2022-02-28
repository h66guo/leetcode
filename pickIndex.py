class Solution:

    def __init__(self, w: List[int]):
        self.prefix=[]
        total=0
        for element in w: 
            total+=element
            self.prefix.append(total)
        self.total=total
        

    def pickIndex(self) -> int:
        target= self.total*random.random()
        low, high= 0, len(self.prefix)
        while low<high: 
            mid=(low+high)//2 
            if target>self.prefix[mid]:
                low=mid+1
            else:
                high=mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
