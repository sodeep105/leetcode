class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        #condition if the list contains one element
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1 or flowerbed[0] == 1 and n==0:
                return True
            else:
                return False
            
            
            
        if flowerbed[0] == 0 and flowerbed[1]==0: #condition for the starting of the array
            flowerbed[0] = 1
            n = n-1
            if n == 0: return True
        m = 1
        while m < len(flowerbed)-1: 
            if flowerbed[m-1] == 0 and flowerbed[m]== 0 and flowerbed[m+1]== 0:
                flowerbed[m] = 1
                n = n-1
                if n == 0: 
                    return True
            
            if m == len(flowerbed)-2: #for the end of the array
                if flowerbed[m] == 0 and flowerbed[m+1] == 0:
                    flowerbed[m] = 1
                    n = n-1
                    if n== 0: return True
                
                
            
            m = m+1
        if n == 0:
            return True
        return False
            