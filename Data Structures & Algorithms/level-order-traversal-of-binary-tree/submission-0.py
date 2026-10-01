# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        res = []
        queue.append(root)

        while len(queue)!= 0:
            subList = []
            for i in range(len(queue)):
                node = queue.popleft()
                
                if (node.left != None): queue.append(node.left)
                if (node.right != None): queue.append(node.right)

                subList.append(node.val)

            res.append(subList) 
        
        return res