class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path= path.split("/")
        print(path)
        for element in path:
            if element=="..":
                if stack:
                    stack.pop()
                    
            elif element=="." or not element:
                continue
                
            else:
                stack.append(element)
        ret= "/" +"/".join(stack)
        
        return ret


