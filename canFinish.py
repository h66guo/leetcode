class Node(object):
    def __init__(self): 
        self.inDegree=0
        self.outNodes=[]

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        graph= defaultdict(Node)
        depth=0
        for element in prerequisites: 
            nextcourse, currentcourse=element[0], element[1]
            graph[nextcourse].inDegree+=1
            graph[currentcourse].outNodes.append(nextcourse)
            depth+=1
            
        queue= deque()
        
        for index, node in graph.items(): 
            print(index)
            if node.inDegree==0: 
                queue.append(index)
        
        removed=0
        while queue: 
            course= queue.pop()
            
            for element in graph[course].outNodes: 
                graph[element].inDegree-=1
                removed+=1
                
                if graph[element].inDegree==0:
                    queue.append(element)
                    
        if removed==depth: 
            return True
        else:
            return False
            
