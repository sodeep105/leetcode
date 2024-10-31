class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        ans = 0
        l = 0
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            while count[s[i]] > 1:
                count[s[l]] -= 1
                l += 1
            newans = i - l +1
            ans = max(ans, newans)
        
        return ans
        