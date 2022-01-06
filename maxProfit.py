import heapq
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        if not inventory or not orders:
            return 0
   
        inventory.sort(reverse=True)
        fullfillPos = self.binarySearch(inventory, orders)
        ans = 0
        for inv in inventory:
            if inv >= fullfillPos:
                ans += (fullfillPos + inv) * (inv - fullfillPos + 1) // 2
            else:
                break
        fullfilled = self.calcNumFullfilled(inventory, fullfillPos)
        if fullfilled < orders and fullfillPos > 1:
            ans += (orders - fullfilled) * (fullfillPos-1)
            
        return ans % (10 ** 9 + 7)
        
    def binarySearch(self, inventory, orders):
        low, high = 1, inventory[0]
        while low + 1 < high:
            mid = (low + high) // 2
            fullfilled = self.calcNumFullfilled(inventory, mid)
            if fullfilled < orders:
                high = mid
            else:
                low = mid
                
        if self.calcNumFullfilled(inventory, low) <= orders:
            return low
        return high
        
    def calcNumFullfilled(self, inventory, mid):
        fullfilled = 0
        for inv in inventory:
            if inv >= mid:
                fullfilled += inv - mid + 1
            else:
                break
                
        return fullfilled
