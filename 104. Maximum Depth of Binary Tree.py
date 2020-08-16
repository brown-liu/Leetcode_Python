'''given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    max=0
    def maxDepth(self, root: TreeNode) -> int:
        self.depth(1,root)
        return self.max

    def depth(self,count,node):
        if node==None:
            return
        if node.left!=None:
            self.depth(count+1,node.left)
        if node.right!=None:
            self.depth(count+1,node.right)
        if count>self.max:
            self.max=count


node=TreeNode()

