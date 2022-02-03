class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if(len(mat)*len(mat[0]) != r*c):
            return mat
        row = 0
        column = 0
        ans = []
        for i in range(0, r):
            temp = []
            ans.append(temp)
            for i in range(0, c):
                temp.append(0)

        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                ans[row][column] = mat[i][j]
                column += 1
                if column == c:
                    row = row+1
                    column = 0

        return ans
        