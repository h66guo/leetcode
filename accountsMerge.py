class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        seen=[False]*len(accounts)
        
        adjacent_dict=defaultdict(list)
        for index, account in enumerate(accounts):
            for i in range(1, len(account)):
                adjacent_dict[account[i]].append(index)
                
        def dfs(account, emailset):
            if seen[account]==True:
                return
            seen[account]=True
            for i in range(1, len(accounts[account])):
                emailset.add(accounts[account][i])
                for element in adjacent_dict[accounts[account][i]]:
                    dfs(element, emailset)
        ret=[]  
        for index, account in enumerate(accounts):
            if seen[index]==True:
                continue
                
            
            emailset=set()
            dfs(index, emailset)
            temp= [account[0]]+sorted(emailset)
            ret.append(temp)
            
        return ret
