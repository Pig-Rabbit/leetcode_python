class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # step 1 - remove any leading whitespace
        while s[0] == ' ':
            s = s[1:]
            if len(s) == 0:
                return 0
        # step 2 - check if the next character is '-' or '+'
        # step 3 - delete non-digit character
        digits = '0123456789'
        sol = ''

        if s[0] == '-' or s[0] == '+':
            if len(s) == 1:
                return 0
            if s[1] not in digits:
                return 0
            else:
                i = 1
                while i < len(s) and s[i] in digits:
                    sol += s[i]
                    i += 1
                final = int(s[0] + sol)
                if final < -2**31:
                    final = -2**31
                elif final > 2**31-1:
                    final = 2**31-1
                return final
        else:
            if len(s) == 0:
                return 0
            if s[0] not in digits:
                return 0
            else:
                i = 0
                while i < len(s) and s[i] in digits:
                    sol += s[i]
                    i += 1
                final = int(sol)
                if final > 2**31-1:
                    final = 2**31-1
                return final
        
        
