class Solution:
    def convert(self, s: str, numRows: int) -> str:
        sol = ''
        i = 0
        if numRows == 1:
            while len(sol) < len(s):
                sol += s[i]
                i += 1
        else:
            cyc = numRows*2 - 2
            for i in range(numRows):
                if i == 0 or i == numRows-1:
                    j = i
                    while j < len(s):
                        sol += s[j]
                        j += cyc
                else:
                    j = i
                    while j < len(s):
                        sol += s[j]
                        if j + cyc - 2*i < len(s):
                            sol += s[j + cyc - 2*i]
                        j += cyc
        
        return sol
