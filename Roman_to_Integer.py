class Solution:
    def romanToInt(self, s: str) -> int:
        a = 0
        i = 0
        while i < len(s):
            if s[i] == 'M':
                a += 1000
            if s[i] == 'D':
                a += 500
            if s[i] == 'C':
                if i+1 < len(s) and s[i+1] == 'M':
                    a += 900
                    i += 1
                elif i+1 < len(s) and s[i+1] == 'D':
                    a += 400
                    i += 1                
                else:
                    a += 100
            if s[i] == 'L':
                a += 50
            if s[i] == 'X':
                if i+1 < len(s) and s[i+1] == 'C':
                    a += 90
                    i += 1
                elif i+1 < len(s) and s[i+1] == 'L':
                    a += 40
                    i += 1
                else:
                    a += 10
            if s[i] == 'V':
                a += 5
            if s[i] == 'I':
                if i+1 < len(s) and s[i+1] == 'X':
                    a += 9
                    i += 1
                elif i+1 < len(s) and s[i+1] == 'V':
                    a += 4
                    i += 1
                else:
                    a += 1
            i += 1
        return a
