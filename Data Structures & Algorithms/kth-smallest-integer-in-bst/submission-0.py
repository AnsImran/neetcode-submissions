class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def find_kthSmallest(root, k, idx, k_val):
            if not root:
                # return
                return idx, k_val                                     # CHANGED
            # find_kthSmallest(root.left, k, idx, k_val)
            idx, k_val = find_kthSmallest(root.left, k, idx, k_val)   # CHANGED
            idx+=1
            if idx == k:
                k_val = root.val
            # find_kthSmallest(root.right, k, idx, k_val)
            idx, k_val = find_kthSmallest(root.right, k, idx, k_val)  # CHANGED
            # return k_val
            return idx, k_val                                         # CHANGED

        # k_val = find_kthSmallest(root, k, 0, None)
        idx, k_val = find_kthSmallest(root, k, 0, None)               # CHANGED

        return k_val
