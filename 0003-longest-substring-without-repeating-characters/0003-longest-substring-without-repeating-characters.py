class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len( s )

        if n == 0 : return 0
        if n == 1 : return 1

        i = j = 0
        dict = { }
        max_ij_len = 0

        while j != n - 1 :
            dict[ s[ j ] ] = j
            j += 1

            if s[ j ] in dict :
                while i < dict[ s[j] ] :
                    dict.pop( s[i] )
                    i += 1
                dict[ s[i] ] = j
                i += 1

            max_ij_len = max( max_ij_len, j - i + 1 )
        return max_ij_len



        """
        n = len( s )

        if n == 0 : return 0
        if n == 1 : return 1
        
        i = j = 0
        dict = { }
        max_ij_len = 0

        while j != n - 1 :
            dict[ s[j] ] = True
            j += 1

            if s[j] in dict :
                for k in range( i, j ) :
                    if s[ k ] == s[ j ] :
                        i = k + 1
                        break
                    else :
                        dict.pop( s[ k ] )

            max_ij_len = max( max_ij_len, j - i + 1 )
        return max_ij_len
        """
