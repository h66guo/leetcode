# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([(root, 0)])
        ret=defaultdict(list)
        while queue:
            node, column = queue.popleft()
            if node!=None:

                ret[column].append(node.val)
                if node.left!=None:
                    queue.append((node.left, column-1))

                if node.right!=None:
                    queue.append((node.right, column+1))
                
        return [ret[x] for x in sorted(ret.keys())]
