# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        self.ret=[]
        def dfs(node,level):
            if not node:
                return
            if level==len(self.ret):
                self.ret.append(node.val)
            
            for element in [node.right, node.left]:
                if element:
                    dfs(element, level+1)
            
        dfs(root, 0)
        
        return self.ret
