class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # for i in nums:
        #     nums.append(i)
        # return nums
        n   = len(nums)-1
        ans    = []
        ans[:] = nums 
        for i in nums:
            ans.append(i)
        return ans




































