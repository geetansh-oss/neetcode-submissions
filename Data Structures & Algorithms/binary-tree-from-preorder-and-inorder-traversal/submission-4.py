# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        mapi = {}
        for i in range(len(inorder)):
            mapi[inorder[i]] = i

        def build(str_pre, end_pre, str_in, end_in):
            if str_pre > end_pre:
                return None

            root = TreeNode(preorder[str_pre])
            mid = mapi[preorder[str_pre]]
            left_num = mid - str_in
            root.left = build(str_pre+1, str_pre+left_num, str_in, mid-1)
            root.right = build(str_pre+left_num+1, end_pre, mid+1, end_in)

            return root
    
        return build(0, len(preorder)-1, 0, len(inorder)-1)
        