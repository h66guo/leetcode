class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=collections.defaultdict(list)
        for element in strs: 
            count=[0]*26
            for char in element: 
                count[ord(char) - ord('a')] += 1
                
            ans[tuple(count)].append(element)
            
        return ans.values()
        
