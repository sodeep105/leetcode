class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        right = k
        res = float(format(sum(nums[left:right]), ".5f"))
        current = res
        for i in range(k,len(nums)):
            current += nums[i]-nums[left]
            res = max(res, current)
            left+=1
        return res/k
        
                