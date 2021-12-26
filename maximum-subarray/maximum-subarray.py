class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSubArr = nums[0]
        maxSum = 0
        for i in range(0, len(nums)):
            if maxSum <0:
                maxSum = 0
            maxSum += nums[i]
            maxSubArr = max(maxSum, maxSubArr)
        return maxSubArr