class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        extra=0
        for element in s:
            if element=="(":
                stack.append(element)
            if element==")" and len(stack)==0:
                extra+=1
                
            elif element==")" and len(stack)>0:
                stack.pop()
                
        return len(stack)+extra
            
