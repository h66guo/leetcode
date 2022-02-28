"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        queue= deque()
        queue.append(p)
        queue.append(q)
        searched=[]
        
        while queue:
            curr=queue.pop()
            if curr not in searched:
                searched.append(curr)
                if curr.parent!= None:
                    queue.append(curr.parent)
                    
            else: 
                return curr
