# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def backtrack_sum(root, targetSum, path):
            if not root:
                return False
            
            path.append(root.val)

            if not root.left and not root.right:
                if sum(path) == targetSum:
                    return True
                else:
                    path.pop()
                    return False
            
            if backtrack_sum(root.left, targetSum, path):
                return True
            if backtrack_sum(root.right, targetSum, path):
                return True
            
            path.pop()

            return False

        path = []

        ans = backtrack_sum(root, targetSum, path)

        return ans


            

















        