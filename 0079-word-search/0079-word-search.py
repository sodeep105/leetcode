class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row, col = len(board), len(board[0])
        path = set()
        def dfs (r,c,i):
            if len(word) == i:
                return True

            if (r>=row or c>=col or r<0 or c<0
                or board[r][c] != word[i] or (r,c)
                in path):
                return False
            
            path.add((r,c))
            result = (dfs(r+1,c,i+1) or
                        dfs(r-1,c,i+1) or
                        dfs(r,c+1,i+1) or
                        dfs(r,c-1,i+1))
            
            path.remove((r,c))
            return result

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        
        return False