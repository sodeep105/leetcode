class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bottom = 0, row-1
        while top <= bottom:
            m = (top+bottom) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bottom = m-1
            
            else:
                break

        if not top <= bottom:
            return False
        
        row= (top+bottom) // 2
        l, r = 0, col-1
        while l <= r:
            mid = (l+r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid -1
            else:
                return True
        
        return False