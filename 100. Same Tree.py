'''Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false'''


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    # Not sure why this not work.
    def isSameTree(self, p, q) -> bool:
        if p.val == None and q.val == None:
            return True

        while p.val != None:
            if q.val == None:
                return False

            if p.val == q.val:
                p.val = p.left
                q.val = q.left
                if p.val == q.val:
                    p.val = p.right
                    q.val = q.right
                else:return False
            else:
                return False
        if q.val != None:
            return False
        else:
            return True
    def isSameTree_submitted(self, p, q) -> bool:
        def isSameTree(self, p, q) -> bool:
            if p == None and q == None:
                return True
            if p == None and q != None:
                return False
            if p != None and q == None:
                return False
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
solution=Solution()
a=TreeNode()
a.val=1
a.left=2
a.right=3

b=TreeNode()
b.val=1
b.left=2
b.right=2
print(solution.isSameTree(a,b))

