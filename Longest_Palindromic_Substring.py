class Solution:
    def longestPalindrome(self, s: str) -> str:
        def around_center(s, L, R):
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            return R-L-1
        
        start = 0
        end = 0
        i = 0
        while i < len(s):
            leng1 = around_center(s, i, i)
            leng2 = around_center(s, i, i+1)
            leng = max(leng1, leng2)
            if leng > end-start+1:
                start = i - (leng-1)//2
                end = i + leng//2
            i += 1
        return s[start:end+1]
