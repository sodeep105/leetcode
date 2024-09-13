class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i = 0 
        j = len(height)-1
        while i < j:
            w = j - i
            if height[i] < height[j]:
                area = height[i]*w
                i+=1
            elif height[j] < height[i]:
                area = height[j]*w
                j-=1
            else:
                area = height[i]*w
                i+=1
            
            maxArea = max(maxArea, area)

        return maxArea
                
            

