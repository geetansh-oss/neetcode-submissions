# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    maxi = 0

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        rh = self.height(root.right)
        lh = self.height(root.left)

        self.maxi = max(self.maxi, rh + lh) 

        return (1 + max(rh, lh))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ht = self.height(root)

        return self.maxi 