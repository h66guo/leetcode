class Solution:
    def uniqueLetterString(self, s: str) -> int:
        map1 = collections.defaultdict(lambda:-1)    # last index for this letter
        map2 = collections.defaultdict(lambda:-1)   # second last index for this letter
        cur = 0
        res = 0
        
        for i, ch in enumerate(s):
            cur += (i - map1[ch]) - (map1[ch] - map2[ch])
            map2[ch] = map1[ch]
            map1[ch] = i
            res += cur
        return res
