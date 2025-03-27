class Solution(object):
    def permute(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        
        res = []
        per = self.permute(nums[1:])
        for p in per:
            for i in range(len(p)+1):
                p_copy = p[:]
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        
        return res
            
        
                 