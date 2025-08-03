class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        n = len( s )
        if n == 0 :
            return True

        idx = 0 
        for i in range( len( t ) ) :

            if s[idx] == t[i] :
                idx += 1
                if idx == n :
                    return True

        return False  