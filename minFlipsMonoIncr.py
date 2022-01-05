class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp=[0]*(len(s))
        numofOnes=int(s[0])
        for i in range(1, len(s)): 
            if s[i]=='1': 
                dp[i]=dp[i-1]
                numofOnes+=1
            if s[i]=='0':
                dp[i]=min(numofOnes, dp[i-1]+1)
                
        return dp[-1]
