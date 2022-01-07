class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones= sum(data)
       
        left=0
        right= left+ones-1
        counter=sum(data[left:right+1])
        maxone=counter
        while right<len(data)-1: 
            
            right+=1
            counter+=data[right]
            counter-=data[left]
            left+=1
            maxone=max(maxone, counter)
            
        return ones-maxone
