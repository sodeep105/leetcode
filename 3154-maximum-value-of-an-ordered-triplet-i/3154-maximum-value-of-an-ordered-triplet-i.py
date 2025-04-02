class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1, len(nums)):
                    new_res = (nums[i]-nums[j])*nums[k]
                    res = max(res, new_res)
        
        if res <0:
            return 0
        else:
            return res
