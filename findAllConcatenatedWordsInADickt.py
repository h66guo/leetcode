class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        def word_break(word):
            dp = [False for _ in range(len(word) + 1)]
            dp[0] = True
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[-1]
        
        res = []
        for word in words:
            # dont consider the current word itself
            # as a word_break
            word_set.remove(word)
            if word and word_break(word):
                res.append(word)
            word_set.add(word)
        
        return res
