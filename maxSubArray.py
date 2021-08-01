def maxSubArray( nums):
        maxSub = nums[0]
        currentSum = 0
        for i in range(0, len(nums)):
            if(currentSum <0):
                currentSum = 0
            currentSum += nums[i]
            maxSub = max(currentSum, maxSub)
            
        return maxSub
nums = [5,4,-1,7,8]
x = maxSubArray(nums)
print(x)