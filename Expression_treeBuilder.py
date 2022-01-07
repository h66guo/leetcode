import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
}


class Node(ABC):
    # @abstractmethod
    def __init__(self, value): 
        self.value= value
        self.left=None
        self.right=None
    # define your fields here
    def evaluate(self) -> int:
        if self.value not in ops: 
            return int(self.value)
        else: 
            return ops[self.value](self.left.evaluate(), self.right.evaluate())


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack=[]
        for element in postfix: 
            node= Node(element)
            if element in ops: 
                node.right=stack.pop()
                node.left= stack.pop()
            stack.append(node)
        return stack[0]
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        
