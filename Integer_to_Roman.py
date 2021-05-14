class Solution:
    def intToRoman(self, num: int) -> str:
        if num//1000 != 0:
            a = num//1000
            res = 'M'*a
        else:
            a = 0
            res = ''
        num -= a*1000 
                
        if num//100 != 0:
            b = num//100
            if b <= 3:
                res += 'C'*b
            elif b == 4:
                res += 'CD'
            elif b >= 5 and b < 9:
                res += 'D' + 'C'*(b-5)
            else:
                res += 'CM'
        else:
            b = 0
        num -= b*100      
                
        if num//10 != 0:
            c = num//10
            if c <= 3:
                res += 'X'*c
            elif c == 4:
                res += 'XL'
            elif c >= 5 and c < 9:
                res += 'L' + 'X'*(c-5)
            else:
                res += 'XC'
        else:
            c = 0
        num -= c*10
        
        if num <= 3:
            res += 'I'*num
        elif num == 4:
            res += 'IV'
        elif num >= 5 and num < 9:
            res += 'V' + 'I'*(num-5)
        else:
            res += 'IX'
        
        return res
        
        
