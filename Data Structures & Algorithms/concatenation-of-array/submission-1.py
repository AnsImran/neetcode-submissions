class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # NOT WORKING SOLUTION
        # infinite loop, avoid it
        # for i in nums:
        #     nums.append(i)
        # return nums
        
        # WORKING SOLUTION - 1
        n       = len(nums)
        ans     = []
        ans[:]  = nums # avoids the loop, copy by value
        ans[n:] = nums
        return ans




































