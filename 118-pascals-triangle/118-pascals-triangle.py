class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]
        for r in range(numRows-1):
            temp = [0] + ans[-1] + [0]
            row = []
            for col in range(len(ans[-1]) + 1):
                row.append(temp[col] + temp[col+1])
            ans.append(row)
                
        
                
        
        return ans
            