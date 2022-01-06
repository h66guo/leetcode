class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        if len(connections) < N-1:
            return -1
        connected_comp=N
        parent = [node for node in range(N + 1)]
        size=[1]*(N+1)
        def find(node):
            while node!=parent[node]:
                parent[node] = parent[parent[node]]
                node=parent[node]
            return node
        
        def union(node1,node2):
            root1,root2=find(node1),find(node2)
            if root1==root2:
                return False
            if size[root1]<size[root2]:
                parent[root1]=root2
                size[root2]+=size[root1]
            else:
                parent[root2] = root1
                size[root1]+=size[root2]
                
            return True
        
        ans = 0
        connections.sort(key = lambda x: x[2])
        for node1,node2,cost in connections:
            if union(node1,node2):
                ans += cost
                connected_comp-=1
    
        return -1 if  connected_comp> 1 else ans
