class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[j]+nums[i] == k: 
                count+=1
                i+=1
                j-=1
            elif nums[j]+nums[i] > k:
                j-=1
            else:
                i+=1
        return count    