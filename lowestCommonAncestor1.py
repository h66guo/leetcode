# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        x = self.lowestCommonAncestor(root.left,p,q)
        y = self.lowestCommonAncestor(root.right,p,q)
        if x and y:
            return root
        if root == p or root == q:
            return root
        if x or y:
            return x or y        
        return None
        
        
        
#         self.found1= False
#         self.found2=False
        
#         def dfs(node):
#             if node==None:
#                 return
#             print(node.val)
#             if self.found1 and self.found2:
#                 return node
            
#             else:
#                 if node==p:
#                     self.found1=True
                    
#                 if node==q:
#                     self.found2=True
                    
                
#                 dfs(node.left)
#                 dfs(node.right)
            
#         return dfs(root)
        
