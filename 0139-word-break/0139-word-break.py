class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def rec( s_idx , i ) :
            nonlocal s , wordDict

            if (s_idx, i ) in memo :
                return memo[ (s_idx ,i ) ]

            if s_idx < 0 or i < 0 or i >= len( wordDict ) :
                return False

            if s[ :s_idx+1] == wordDict[i] :
                return True

            f_idx = s_idx - len( wordDict[i] ) + 1
            res = False

            if s[ f_idx : s_idx+1 ] == wordDict[i] :
                res = rec( f_idx-1 , i ) or rec( f_idx-1 , i-1 )
                #for j in range( i+1 , len( wordDict ) ) :
                res = res or rec( f_idx-1 , len(wordDict)-1 )

            res = res or rec( s_idx , i-1 )

            memo[ ( s_idx , i ) ] = res
            return res

        return  rec( len( s )-1 , len( wordDict )-1 )