class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        sumarry=[0 for i in range(length)]
        for element in updates:
            
            start, end, incre= element[0], element[1], element[2]
            sumarry[start]+=incre
            if end<length-1: 
                sumarry[end+1]-=incre
       
        for i in range(1, length): 
            
            sumarry[i]=sumarry[i]+ sumarry[i-1]
        return sumarry
