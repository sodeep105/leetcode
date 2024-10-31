class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        add = 0
        res = float('inf')

        for r in range(len(nums)):
            
            add += nums[r]
            while add >= target:
                newres = r-l+1
                res = min(newres, res)
                add -= nums[l]
                l = l+1
                
            
        if res != float('inf'):
            return res
        else: 
            return 0




        