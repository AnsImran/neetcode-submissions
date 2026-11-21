class Solution:
    def rob(self, nums: List[int]) -> int:
        def dpm(i, nums, cache):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i]+dpm(i+2, nums, cache), dpm(i+1, nums, cache))
            return cache[i]
        
        ans = dpm(0, nums, {})
        return ans
