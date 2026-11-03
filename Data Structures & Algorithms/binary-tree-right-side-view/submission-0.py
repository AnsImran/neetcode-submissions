from collections import deque
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
        
        q         = deque([root])
        main_list = []

        while len(q) > 0:
            len_of_level = len(q)
            for i in range(len_of_level):
                curr = q.popleft()
                if i == len_of_level - 1:
                    main_list.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return main_list
            






        