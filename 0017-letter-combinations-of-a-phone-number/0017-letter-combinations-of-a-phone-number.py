class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        memo = {'2' :"abc" ,
            '3' : "def" ,
            '4' : "ghi" ,
            '5' :"jkl" ,
            '6' : "mno" ,
            '7' : "pqrs" ,
            '8' : "tuv" ,
            '9' : "wxyz" }
        result = []

        def rec( res , idx ) :
            if idx >= len( digits ) :
                result.append( res )
                return

            for letter in  memo[digits[idx]] :
                rec( res+letter , idx + 1 )

        rec( "" , 0 )
        return result