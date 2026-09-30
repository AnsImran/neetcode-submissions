class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
            return
        nums1[n:] = nums1[:m]
        i  = 0
        i2 = n
        i3 = 0
        while i2<=m+n-1 and i3<=n-1:
            if nums1[i2] <= nums2[i3]:
                nums1[i] = nums1[i2]
                i+=1
                i2+=1
                if not i2<=m+n-1:
                    nums1[i:] = nums2[i3:]
            else:
                nums1[i] = nums2[i3]
                i+=1
                i3+=1

# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         nums1[n:] = nums1[:m]                 # shift the m real values to the BACK
#         i, i2, i3 = 0, n, 0                   # write / read-left / read-right

#         while i2 <= m+n-1 and i3 <= n-1:      # FIX 1: 'and' — stop when either side empties
#             if nums1[i2] <= nums2[i3]:
#                 nums1[i] = nums1[i2]; i += 1; i2 += 1
#             else:
#                 nums1[i] = nums2[i3]; i += 1; i3 += 1

#         while i3 <= n-1:                      # FIX 2: leftovers after the loop, written at i
#             nums1[i] = nums2[i3]; i += 1; i3 += 1
#         # leftover LEFT values need no work — they are already sitting at i2..end in order
#                                               # FIX 3: no return statement at all
