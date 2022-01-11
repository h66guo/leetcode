import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        d={}
        for element in s: 
            if element in d: 
                d[element]+=1
            else:
                d[element]=1
        l=[]    
        for element in d: 
            temp= [-d[element],element]
            l.append(temp)
            
        heapq.heapify(l)
        
        ans=""
        
        while len(l)>1: 
            temp1= heapq.heappop(l)
            temp2=heapq.heappop(l)
            ans+=temp1[1]
            ans+=temp2[1]
            
            if temp1[0]!=-1: 
                heapq.heappush(l, [temp1[0]+1, temp1[1]])
                
                
            if temp2[0]!=-1: 
                heapq.heappush(l, [temp2[0]+1, temp2[1]])
                
        if len(l)==0:
            return ans
        
        if l[0][0]==-1: 
            temp=l.pop()
            ans+=temp[1]
            return ans
        
        else:
            return ""
