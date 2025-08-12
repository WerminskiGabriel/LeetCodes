class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len( s )
        wd_len = max( map( len , wordDict ) )
        dp = [False] * ( n+1 )
        dp[0] = True
        wordDict = dict.fromkeys( wordDict , 0 )

        for i in range( 1 ,  n+1 ) :
            for j in range( i-1 , max( -1 , i-wd_len-1 ) , -1 ) : 
                if dp[j] and s[j:i] in wordDict :
                    dp[i] = True
                    break
        return dp[n]