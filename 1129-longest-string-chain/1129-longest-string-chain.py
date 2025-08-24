class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len( words )
        words = sorted( words, key = lambda x : len( x ) )
        memo = { }
        res = 1
        for word in words :
            memo[word] = 1

            for i in range( len(word) ) :
                pre = word[:i] + word[i+1:]
                if pre in memo :
                    memo[word] = max( memo[word] , memo[pre] +1 )
                    res = max( res , memo[word] )
        return res