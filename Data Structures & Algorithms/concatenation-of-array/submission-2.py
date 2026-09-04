class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # NOT WORKING SOLUTION
        # infinite loop, avoid it
        # for i in nums:
        #     nums.append(i)
        # return nums
        
        # # WORKING SOLUTION - 1
        # ans    = []
        # ans[:] = nums # avoids the loop, copy by value
        # for i in nums:
        #     ans.append(i)
        # return ans

        # # WORKING SOLUTION - 2
        # n       = len(nums)
        # ans     = []
        # ans[:]  = nums # avoids the loop, copy by value
        # ans[n:] = nums
        # return ans

        # WORKING SOLUTION - 3
        ans    = []
        ans[:] = nums + nums
        return ans










































































