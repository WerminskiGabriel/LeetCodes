class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0 
        while a or b or c :
            
            if (c & 1) == 0 :
                if ( a& 1 ) == 1 :
                    cnt += 1
                if ( b & 1 ) == 1 :
                    cnt += 1
            
            elif ( a & 1 ) == 0 and ( b & 1 ) == 0 :
                cnt += 1

            a = a >> 1
            b = b >> 1 
            c = c >> 1
        return cnt 