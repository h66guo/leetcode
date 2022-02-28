"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        first, last=None, None
    
        def trav(node):
            nonlocal first, last
            if node:
                # left
                trav(node.left)
                # node
                
                if last: 
                    last.right=node
                    node.left= last
                    
                else:
                    first= node
                    
                last=node
                
#               right
                trav(node.right)
                
        if not root:
            return None
        
        trav(root)
        
        last.right= first
        first.left=last
        return first
                
                
                
                
