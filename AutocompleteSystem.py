class Trie:
    
    def __init__(self):
        self.trie = {}
        self.time = 0
        self.is_word = False
        
    def add_sentence(self, sentence, time):
        node = self
        for c in sentence:
            if not c in node.trie:
                node.trie[c] = Trie()
            node = node.trie[c]
        node.time += time
        node.is_word = True

        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self._input = ""
        for sentence, time in zip(sentences, times):
            self.trie.add_sentence(sentence, time)     

    def input(self, c: str) -> List[str]:
        
        if c == "#":
            self.trie.add_sentence(self._input, 1)
            self._input = ""
            return []
        
        self._input += c
        
        raw_res = []
        node = self.trie
        for char in self._input:
            if not char in node.trie:
                return []
            node = node.trie[char]
        
        raw_res = []
        
        def get_sentence(node, word):
            if node.is_word:
                raw_res.append([-node.time, word])
                
            for k, n in node.trie.items():
                get_sentence(n, word+k)
        
        get_sentence(node, self._input)
      
        raw_res.sort()
        
        return [sentence for _, sentence in raw_res[:3]]
