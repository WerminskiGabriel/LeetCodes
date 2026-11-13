class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin( a )[2:] 
        b = bin( b )[2:]
        c = bin( c )[2:]

        cnt = 0 
        
        idx = 1
        while idx <= len( c ) and idx <= len( b ) and idx <= len( a ) : 
            if c[-idx] == '0' :
                if a[-idx] == '1':
                    cnt += 1 
                if b[-idx] == '1':
                    cnt += 1 
            elif a[-idx] == '0' and b[-idx] == '0' :
                cnt += 1 
            idx += 1
        while idx <= len(c) and idx <= len(b) :
            if c[-idx] != b[-idx] :
                cnt += 1
            idx += 1
        while idx <=len(c) and idx <= len(a) :
            if c[-idx] != a[-idx] :
                cnt += 1
            idx += 1

        while idx <=len(b) and idx <= len(a) :
            if b[-idx] == '1':
                cnt += 1
            if a[-idx] == '1':
                cnt += 1
            idx += 1


        while idx <= len(c) :
            if c[-idx] == '1' :
                cnt += 1 
            idx += 1
        while idx <= len(a) :
            if a[-idx] == '1' :
                cnt += 1 
            idx += 1
        while idx <= len(b) :
            if b[-idx] == '1' :
                cnt += 1 
            idx += 1
        return cnt 