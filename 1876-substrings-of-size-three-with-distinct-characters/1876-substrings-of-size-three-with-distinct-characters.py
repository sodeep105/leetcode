class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        count = 0
        if len(s) < 3:
            return 0
        for i in range(len(s)):
            dic[s[i]]= dic.get(s[i], 0) + 1     
            if i>=2:
                if len(dic.values()) == 3:
                    count+=1
                dic[s[i-2]] -= 1
                if dic[s[i-2]] == 0:
                    dic.pop(s[i-2])
                
                
        return count