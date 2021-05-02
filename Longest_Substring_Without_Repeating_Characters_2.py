class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = j = 0
        res = {}
        max_len = 0
        while j < n:
            while s[j] in res:
                res.remove(s[i])
                i += 1
            
            res = set(s[i:j+1])
            j += 1
            max_len = max(max_len, len(res))
        return max_len
