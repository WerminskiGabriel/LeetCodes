class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin( a )[2:] 
        b = bin( b )[2:]
        c = bin( c )[2:]
        
        max_len = max( len( a ), len(b), len(c) )

        a = a.zfill(max_len)
        b = b.zfill(max_len)
        c = c.zfill(max_len)

        cnt = 0 
        idx = 1
        while idx <= max_len: 
            if c[-idx] == '0' :
                if a[-idx] == '1':
                    cnt += 1 
                if b[-idx] == '1':
                    cnt += 1 
            elif a[-idx] == '0' and b[-idx] == '0' :
                cnt += 1 
            idx += 1

        return cnt 