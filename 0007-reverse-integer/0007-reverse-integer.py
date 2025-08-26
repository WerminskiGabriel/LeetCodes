class Solution:
    def reverse(self, x: int) -> int:
        
        negative = True if x < 0 else False
        y = 0
        if negative :
            x = -x
        while x > 0 :
            y = y*10 + x % 10
            x //= 10
        y *= y < 2 ** 31
        if negative :
            y = -y
        return y