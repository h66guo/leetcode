class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
		#Data handling and sorting by timestamp
        data = list(zip(username, timestamp, website))
        data.sort(key=lambda a:a[1])
        
        userHist = defaultdict(list)
        for u, t, w in data:
            userHist[u].append(w)
        
        patterns = defaultdict(int)
        for u, h in userHist.items():
            if len(h) < 3:
                continue
                
            visited = set() #to ensure one pattern per user
            a = 0
            for i in range(0,len(h)):
                b = i+1
                for j in range(b, len(h)):
                    c = j+1
                    for k in range(c,len(h)):
                        if (h[i], h[j], h[k]) not in visited:
                            patterns[(h[i], h[j], h[k])] += 1
                            visited.add((h[i], h[j], h[k]))
        
        #Retrieving max score patterns and then sorting them
        #No need to sort ALL patterns, only ones with max score
        maxPatScore = patterns[max(patterns, key=lambda k: patterns[k])]
        allMaxPatterns = []
        for u,h in patterns.items():
            if patterns[u]==maxPatScore:
                allMaxPatterns.append(u)
        allMaxPatterns.sort()
        
        return allMaxPatterns[0]
