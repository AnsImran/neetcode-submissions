def custom_dict(op:str, val:str, counts_dict):
    if op == 'insert':
        if counts_dict.get(val):
            counts_dict[val] += 1
        else:
            counts_dict[val]  = 1
    elif op == 'read':
        if counts_dict.get(val):
            return counts_dict[val]
        else:
            return None

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts_dict = {}

        for i in nums:
            custom_dict('insert', i, counts_dict)
        
        i = 0

        for key in [0,1,2]:
            val = custom_dict('read', key, counts_dict)
            if val:
                for j in range(val):
                    nums[i]  = key
                    i       += 1
            else:
                continue




























