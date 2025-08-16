class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        original = strs.copy()
        n = len( strs )

        for i in range( n ) :
            strs[i] = ( "".join(sorted( strs[i] ) ) , i )
        strs.sort()
        result = {}

        for i in range( n ) : #in strs
            st , idx = strs[i][0] , strs[i][1]
            orig = original[ idx ]
            
            if st in result :
                result[st].append( orig )
            else :
                result[ st ] = [orig]
        return list( result.values() )