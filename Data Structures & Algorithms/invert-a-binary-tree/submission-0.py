class Solution:

    def invert(self, node: Optional[TreeNode]):
        if not node:
            return

        temp = node.left
        node.left = node.right
        node.right = temp

        self.invert(node.left)
        self.invert(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root