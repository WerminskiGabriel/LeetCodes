class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        original = strs.copy()
        n = len( strs )

        for i in range( n ) :
            strs[i] = ( sorted( strs[i] ) , i )
        strs.sort()
        result = []

        current = strs[0][0]
        start = 0
        for i in range( n ) :
            if current != strs[i][0] :
                res = []
                for j in range( start , i ) :
                    res.append( original[ strs[j][1]] )
                result.append( res.copy() )
                start = i
                current = strs[i][0]
        res = []
        for j in range( start , n ) :
            res.append( original[ strs[j][1] ] )
        result.append( res )
        return result