# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:  # bfs
        adj= collections.defaultdict(list)
        res= []
        def tograph(root):
            if not root: return 
            if root.left:    
                adj[root.val].append(root.left.val)
                adj[root.left.val].append(root.val)
            if root.right:
                adj[root.val].append(root.right.val)
                adj[root.right.val].append(root.val)
            tograph(root.left)
            tograph(root.right)
        tograph(root)

        def bfs(t, k):
            visit = set()
            q = collections.deque([t])
            visit.add(t)
            while q and k > 0:
                # print(f'k - {k}')
                size = len(q)
                k -= 1 
                # print(list(q))
                for i in range(size):
                    temp = q.popleft()
                    # print(f'temp - {temp}')
                    for j in adj[temp]:
                        if j not in visit:
                            q.append(j)
                            visit.add(j)
            return list(q)
        return bfs(target.val, k)
