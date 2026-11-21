class Solution:
    def climbStairs(self, n: int) -> int:
        def dpm(n, cache):
            if n<4:
                return n
            if n in cache:
                return cache[n]
            cache[n] = dpm(n-1, cache) + dpm(n-2, cache)
            return cache[n]

        ans = dpm(n, {})
        return ans

        

            
