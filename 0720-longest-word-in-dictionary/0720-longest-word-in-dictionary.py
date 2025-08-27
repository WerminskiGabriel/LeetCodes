class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()

        memo = {}
        res = ""
        for word in words :

            prefix = word[:len(word)-1]
            if prefix in memo :
                memo[word] = 0
                if len( res ) < len( word ) :
                    res = word
            elif len( word ) == 1 :
                memo[word] = 0
                if res == "" :
                    res = word
        return res 