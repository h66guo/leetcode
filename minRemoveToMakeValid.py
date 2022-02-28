class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        toRemove= set()
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            if s[i]=="(":
                stack.append(i)
              
            elif not stack:
                toRemove.add(i)
                
            else:
                stack.pop()
                
           
              
        toRemove=toRemove.union(set(stack))
        
        string_builder=[]
        for i, c in enumerate(s):
            if i not in toRemove:
                string_builder.append(c)
        return "".join(string_builder)
                
            
