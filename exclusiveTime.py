class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        
        ret=[0]*n
        for element in logs:
            element= element.split(':')
            print(stack)
            if stack:
                if element[1]=="start":
                    ret[int(stack[-1][0])]+=int(element[2])-int(prev)
                else:
                    ret[int(stack[-1][0])]+=int(element[2])-int(prev)+1
                
            if element[1]=="start":
                # if stack and element[0]!=stack[-1][0]:
                    
                stack.append([element[0], element[2]])
                
            else:
                stack.pop()
                
            prev=element[2]
                
        return ret
                
                
