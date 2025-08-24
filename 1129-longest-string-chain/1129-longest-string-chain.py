class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n =  len( words )
        words = sorted( words , key = lambda x : len( x ) )
        
        memo = {}
        def is_predecessor( pre , par ) :
            if (pre,par) in memo:
                return memo[ (pre,par) ]

            lena = len( pre )
            lenb = len( par )

            if lena + 1 != lenb :
                memo[ (pre,par) ] = False 
                return False

            for i in range( lena ) :
                a = par[:i]+par[i+1:]
                if pre == a :
                    memo[ (pre,par) ] = True
                    return True
            a = par[:lenb-1]
            memo[ (pre,par) ] = (pre == a)
            return memo[ (pre,par) ]

        cnt = 1
        res = 0
        dp = [1] * n
        max_val = 1
        for i in range( 1, n ) :
            for j in range( i-1 , -1 , -1 ) :
                if len( words[j] ) == len( words[i] ) :
                    continue
                if len( words[j] ) != len( words[i] )-1 :
                    break
                if is_predecessor( words[j] , words[i] ) :
                    dp[i] = max( dp[i] , dp[j]+1 )
                    max_val = max( max_val , dp[i] )

        return max_val