'''Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    class Solution:
        def levelOrderBottom(self, root: TreeNode):
            if not root:
                return []
            result = []
            seeifmt = [root]
            while seeifmt:
                listcarryseeifmt = []
                listcarrycurrentandnext = []
                for node in seeifmt:
                    listcarrycurrentandnext.append(node.val)
                    if node.left:
                        listcarryseeifmt.append(node.left)
                    if node.right:
                        listcarryseeifmt.append(node.right)
                seeifmt = listcarryseeifmt
                result.append(listcarrycurrentandnext)
            return result[::-1]

