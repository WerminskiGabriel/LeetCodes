class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        original = strs.copy()
        n = len( strs )
        def hash( str ) :
        #   poynomaial rolling hash algo :
            res = 0
            m = 1e9+7
            power = 1
            q = 31

            for i in range( len( str ) ) :
                res = ( res + ord( str[i] ) * power ) % m
                power = ( power * q ) % m
            return int( res )

        for i in range( n ) :
            strs[i] = ( sorted( strs[i] ) , i )
        strs.sort()
        result = []
        strs = [ ( hash( str[0] ) , str[1] ) for str in strs ]

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