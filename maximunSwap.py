class Solution:
    def maximumSwap(self, num: int) -> int:
        num= list(str(num))
        max_index= len(num)-1
        start=end= 0
        
        for i in range(len(num)-1, -1, -1):
            if num[i]>num[max_index]:
                max_index=i
                
            elif num[i]<num[max_index]:
                start=i
                end=max_index
                
        num[start], num[end]=num[end], num[start]
        
        return int(''.join(num))
