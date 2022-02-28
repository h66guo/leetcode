class Solution:
    def validPalindrome(self, s: str) -> bool:
        counter=0
        first, last= 0, len(s)-1
        while first<last:
            if s[first]!=s[last]:
                counter+=1
                
                if counter>1:
                    return False
                
                if s[last-1]==s[first] and s[first+1]==s[last]:
                    first+=1
                    last-=1
                    counter-=1
            
                elif s[first]==s[last-1]:
                    last-=1
                    
                elif s[first+1]==s[last]:
                    first+=1
                    
                else:
                    return False
            else:
                first+=1
                last-=1
                
        return True
