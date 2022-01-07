class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def backtrack(current, remain_open, remain_close):
            print(current)
            if remain_open == 0 and remain_close == 0:
                self.res.append(current)
                return
            
            if remain_open == remain_close:
                current += '('
                backtrack(current, remain_open-1, remain_close)
                current = current[:-1]
            else:
                if remain_open > 0:
                    current += '('
                    backtrack(current, remain_open-1, remain_close)
                    current = current[:-1]
                current += ')'
                backtrack(current, remain_open, remain_close-1)
                current = current[:-1]
        
        backtrack('', n, n)
        
        return self.res
