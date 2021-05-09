class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            plus = 1
        else:
            plus = 0
        str_x = str(abs(x))
        rev_x = ''
        for i in str_x:
            rev_x = i + rev_x
        sol = int(rev_x)
        if plus == 1 and sol > 2**31 -1:
            return 0
        elif plus == 1 and sol <= 2**31 -1:
            return sol
        elif plus == 0 and sol > 2**31:
            return 0
        elif plus == 0 and sol <= 2**31:
            return -sol
