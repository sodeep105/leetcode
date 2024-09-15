class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastZero = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[lastZero] = nums[i]
                lastZero+=1
        
        for i in range(lastZero, len(nums)):
            nums[i] = 0

        return nums