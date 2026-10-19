# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_recursion(root, inorder_list):
    if not root:
        return
    inorder_recursion(root.left,  inorder_list)
    inorder_list.append(root.val)
    inorder_recursion(root.right, inorder_list)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_list = [] 
        inorder_recursion(root, inorder_list)
        return inorder_list






        