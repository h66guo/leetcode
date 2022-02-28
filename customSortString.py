class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count= collections.Counter(s)
        ans=[]
        for element in order:
            if element in count:
                ans.append(element*count[element])
                
                count[element]=0
                
        for element in count:
            ans.append(element*count[element])
            
        return "".join(ans)
