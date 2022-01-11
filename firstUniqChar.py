class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for element in s: 
            if element in count: 
                count[element]+=1
            else:
                count[element]=1
        print(count)      
        for element in s: 
            if count[element]==1: 
                return s.index(element)
            
        return -1
