# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []

        while len(queue) != 0:
            right_node = int()
            for i in range(len(queue)):
                node = queue.popleft() 

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                right_node = node

            res.append(right_node.val)
        
        return res