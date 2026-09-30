# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    isEqual = True

    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return 

        if not p or not q:
            self.isEqual = False
            return

        if(p.val != q.val):
            self.isEqual = False

        self.isSame(p.left, q.left)
        self.isSame(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        self.isSame(p,q)

        return self.isEqual

        
        