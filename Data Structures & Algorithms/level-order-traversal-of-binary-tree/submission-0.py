from collections import deque
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
        
        q         = deque([root])
        main_list = []

        while len(q) > 0:
            sublist = []
            for i in range(len(q)):
                curr = q.popleft()
                sublist.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            main_list.append(sublist)
        return main_list
        