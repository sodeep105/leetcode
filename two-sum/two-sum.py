class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = {}
        for i in range(0,len(nums)):
            find = target - nums[i]
            if find in mydict.keys():
                return mydict[find],i
            mydict[nums[i]] = i
        